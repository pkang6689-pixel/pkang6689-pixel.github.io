#!/usr/bin/env python3
"""
Fix Physics lesson files to match Chemistry reference implementation.
Fixes:
1. CSS link format consistency
2. Adds proper video data structure
3. Normalizes rubric colors and metadata
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Tuple

# Video metadata for Physics lessons (by lesson identifier u[unit]_l[lesson])
PHYSICS_VIDEO_DATA = {
    "u1_l1.1": {
        "primary_video": {
            "id": "6PcN6A7hs4A",
            "title": "Khan Academy - Intro to Physics",
            "src": "https://www.youtube.com/embed/6PcN6A7hs4A?start=0",
            "difficulty_color": "#7FFF00", "difficulty_rating": "Easy-Medium",
            "detail_color": "#90EE90", "detail_rating": "Medium-Low",
            "speed_color": "#87CEEB", "speed_rating": "Fast",
            "pace_color": "#87CEEB", "pace_rating": "Fast"
        },
        "videos": [
            {
                "id": "6PcN6A7hs4A",
                "title": "Khan Academy - Intro to Physics",
                "src": "https://www.youtube.com/embed/6PcN6A7hs4A?start=0",
                "difficulty_color": "#7FFF00", "difficulty_rating": "Easy-Medium",
                "detail_color": "#90EE90", "detail_rating": "Medium-Low",
                "speed_color": "#87CEEB", "speed_rating": "Fast",
                "pace_color": "#87CEEB", "pace_rating": "Fast"
            },
            {
                "id": "w7HeAUk2Foc",
                "title": "Organic Chemistry Tutor",
                "src": "https://www.youtube.com/embed/w7HeAUk2Foc?start=0",
                "difficulty_color": "#FFA500", "difficulty_rating": "Medium-Hard",
                "detail_color": "#FFA500", "detail_rating": "Medium-High",
                "speed_color": "#FFD700", "speed_rating": "Medium",
                "pace_color": "#FF4500", "pace_rating": "Slow"
            }
        ]
    }
}

class PhysicsLessonFixer:
    def __init__(self, base_path: str = "ArisEdu Project Folder/PhysicsLessons"):
        self.base_path = Path(base_path)
        self.all_units = sorted([d for d in self.base_path.iterdir() if d.is_dir() and d.name.startswith("Unit")])
        
    def get_lesson_id(self, unit_num: int, lesson_num: str) -> str:
        """Generate lesson ID like u1_l1.1"""
        return f"u{unit_num}_l{lesson_num}"
    
    def fix_css_link(self, content: str) -> str:
        """Fix CSS link format to match Chemistry reference"""
        # Change from: <link rel="stylesheet" href="/ArisEdu Project Folder/styles/main.css">
        # To: <link href="/ArisEdu Project Folder/styles/main.css" rel="stylesheet"/>
        pattern = r'<link rel="stylesheet" href="/ArisEdu Project Folder/styles/main\.css">'
        replacement = '<link href="/ArisEdu Project Folder/styles/main.css" rel="stylesheet"/>'
        return re.sub(pattern, replacement, content)
    
    def get_video_data_for_lesson(self, lesson_id: str) -> Dict:
        """Get video data for a specific lesson"""
        if lesson_id in PHYSICS_VIDEO_DATA:
            return PHYSICS_VIDEO_DATA[lesson_id]
        
        # Return generic default data for lessons not yet customized
        return {
            "primary_video": {
                "id": "dummyid",
                "title": "Video Lecture",
                "src": "#",
                "difficulty_color": "#87CEEB", "difficulty_rating": "Medium",
                "detail_color": "#87CEEB", "detail_rating": "Medium",
                "speed_color": "#87CEEB", "speed_rating": "Medium",
                "pace_color": "#87CEEB", "pace_rating": "Medium"
            },
            "videos": []
        }
    
    def generate_videos_panel_html(self, videos_data: Dict) -> str:
        """Generate videos panel HTML with proper structure"""
        videos = videos_data.get("videos", [])
        if not videos:
            # Fallback to primary video only
            primary = videos_data.get("primary_video", {})
            videos = [primary] if primary else []
        
        panel_html = '<div class="videos-panel-title">Lesson videos</div>'
        
        for video in videos[:5]:  # Limit to 5 videos
            video_id = video.get("id", "")
            title = video.get("title", "Video")
            src = video.get("src", "#")
            diff_color = video.get("difficulty_color", "#87CEEB")
            detail_color = video.get("detail_color", "#87CEEB")
            speed_color = video.get("speed_color", "#87CEEB")
            pace_color = video.get("pace_color", "#87CEEB")
            diff_rating = video.get("difficulty_rating", "Medium")
            detail_rating = video.get("detail_rating", "Medium")
            speed_rating = video.get("speed_rating", "Medium")
            pace_rating = video.get("pace_rating", "Medium")
            
            # Escape special characters in title and URL
            title_escaped = title.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            src_escaped = src.replace("&", "&amp;")
            
            panel_html += f'''<div class="videos-panel-item"><a data-color-detail="{detail_color}" data-color-difficulty="{diff_color}" data-color-pace="{pace_color}" data-color-speed="{speed_color}" data-rating-detail="{detail_rating}" data-rating-difficulty="{diff_rating}" data-rating-pace="{pace_rating}" data-rating-speed="{speed_rating}" data-video-id="{video_id}" data-video-src="{src_escaped}" data-video-title="{title_escaped}" href="{src_escaped}" target="_blank">{title_escaped}</a><div aria-hidden="true" class="mini-rubric"><span style="background:{diff_color}"></span><span style="background:{detail_color}"></span><span style="background:{speed_color}"></span><span style="background:{pace_color}"></span></div></div>'''
        
        return panel_html
    
    def fix_video_file(self, file_path: Path, unit_num: int, lesson_num: str, file_type: str) -> bool:
        """Fix a single video lesson file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Fix CSS link format
            content = self.fix_css_link(content)
            
            # For Video files, also fix/populate video data
            if file_type == "_Video.html":
                # Get video data
                lesson_id = self.get_lesson_id(unit_num, lesson_num)
                video_data = self.get_video_data_for_lesson(lesson_id)
                primary_video = video_data.get("primary_video", {})
                
                # Replace empty video embed with actual embed
                embed_pattern = r'<div class="video-embed">\s*</div>'
                if primary_video.get("src") and primary_video["src"] != "#":
                    src = primary_video["src"].replace("&", "&amp;")
                    new_embed = f'''<div class="video-embed"><iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen="" referrerpolicy="strict-origin-when-cross-origin" src="{src}" title="Video Lecture"></iframe></div>'''
                else:
                    new_embed = '<div class="video-embed"></div>'
                content = re.sub(embed_pattern, new_embed, content)
                
                # Replace videos panel - more comprehensive pattern to catch all variants
                # This pattern captures the entire videos-panel including all old video items
                old_panel_pattern = r'<div aria-hidden="true" class="videos-panel">.*?(?=<a class="side-button" href="Lesson \d+\.\d+\.?\d?_Summary\.html")'
                
                new_videos_panel = self.generate_videos_panel_html(video_data)
                
                content = re.sub(old_panel_pattern, f'<div aria-hidden="true" class="videos-panel">{new_videos_panel}</div>\n', 
                                content, flags=re.DOTALL)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return True
        except Exception as e:
            print(f"Error fixing {file_path}: {e}")
            return False
    
    def process_all_lessons(self):
        """Process all Physics lesson files"""
        total_files = 0
        fixed_files = 0
        
        for unit_dir in self.all_units:
            unit_num = int(unit_dir.name.replace("Unit", ""))
            print(f"\nProcessing {unit_dir.name}...")
            
            # Find all lesson files in this unit
            lesson_files = sorted([f for f in unit_dir.iterdir() if f.is_file() and "Lesson" in f.name])
            
            for lesson_file in lesson_files:
                filename = lesson_file.name
                
                # Extract lesson number (e.g., "1.1" from "Lesson 1.1_Video.html")
                lesson_match = re.search(r'Lesson (\d+(?:\.\d+)?)', filename)
                if not lesson_match:
                    continue
                
                lesson_num = lesson_match.group(1)
                
                # Identify file type
                if "_Video.html" in filename:
                    file_type = "_Video.html"
                elif "_Summary.html" in filename:
                    file_type = "_Summary.html"
                elif "_Practice.html" in filename:
                    file_type = "_Practice.html"
                elif "_Quiz.html" in filename:
                    file_type = "_Quiz.html"
                else:
                    continue
                
                # Fix the file
                total_files += 1
                if self.fix_video_file(lesson_file, unit_num, lesson_num, file_type):
                    fixed_files += 1
                    print(f"  ✓ Fixed: {filename}")
                else:
                    print(f"  ✗ Error: {filename}")
        
        print(f"\n{'='*50}")
        print(f"Summary: Fixed {fixed_files}/{total_files} lesson files")
        print(f"{'='*50}")

def main():
    # Change to the workspace root
    workspace_root = Path(__file__).parent
    os.chdir(workspace_root)
    
    fixer = PhysicsLessonFixer()
    fixer.process_all_lessons()
    print("\nPhysics lesson files have been fixed!")

if __name__ == "__main__":
    main()
