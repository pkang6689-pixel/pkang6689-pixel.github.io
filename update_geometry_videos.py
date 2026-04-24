"""Update Geometry lesson video pages with real video data."""
import os
import re

BASE = r"c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\CourseFiles\GeometryLessons"

DIFF_COLOR = {"Easy":"#90EE90","Medium-Easy":"#7FFF00","Medium":"#FFA07A","Medium-Hard":"#FF6347","Hard":"#FF4500"}
DET_COLOR  = {"Low":"#7FFF00","Medium-Low":"#90EE90","Medium":"#FFD700","Medium-High":"#FFA500","High":"#FF4500"}
SPD_COLOR  = {"Very Fast":"#87CEEB","Fast":"#87CEEB","Medium-Fast":"#87CEEB","Medium":"#FFD700","Medium-Long":"#FFA07A","Long":"#FF4500"}
PACE_COLOR = {"Fast":"#87CEEB","Medium":"#90EE90","Slow":"#FF4500"}

def dc(d): return DIFF_COLOR[d]
def ec(d): return DET_COLOR[d]
def sc(d): return SPD_COLOR[d]
def pc(d): return PACE_COLOR[d]

def v(channel, vid_id, watch_url, diff, det, spd, pace, embed_extra=""):
    """Build a video dict."""
    embed = f"https://www.youtube.com/embed/{vid_id}{embed_extra}"
    return {
        "channel": channel, "id": vid_id, "embed": embed,
        "watch": watch_url,
        "diff": diff, "det": det, "spd": spd, "pace": pace
    }

# Lesson data: {lesson_key: (unit_dir, file, summary_file, [videos])}
# First video in list = primary (goes in iframe and rubric-data)
LESSONS = {
    "1.1": ("Unit1", "Lesson1.1_Video.html", "Lesson1.1_Summary.html", [
        v("The Organic Chemistry Tutor","dDWjhRfBsKM","https://www.youtube.com/watch?v=dDWjhRfBsKM","Medium-Easy","Medium-High","Medium-Fast","Medium"),
        v("Professor Dave","JHMB_ob89qs","https://www.youtube.com/watch?v=JHMB_ob89qs","Medium","Medium","Fast","Medium"),
        v("Khan Academy","JcqCf762y9w","https://www.youtube.com/watch?v=JcqCf762y9w","Medium-Easy","Medium","Fast","Medium"),
        v("Khan Academy","J2Qz-7ZWDAE","https://www.youtube.com/watch?v=J2Qz-7ZWDAE","Medium","Medium-High","Medium","Medium"),
    ]),
    "2.1": ("Unit2", "Lesson2.1_Video.html", "Lesson2.1_Summary.html", [
        v("Tarver Academy","tPJgCh9FHNI","https://www.youtube.com/watch?v=tPJgCh9FHNI","Easy","Low","Fast","Fast"),
    ]),
    "2.2": ("Unit2", "Lesson2.2_Video.html", "Lesson2.2_Summary.html", [
        v("The Organic Chemistry Tutor","TCBu8PD4Lls","https://www.youtube.com/watch?v=TCBu8PD4Lls&t=3s","Medium-Hard","High","Long","Slow","?start=3"),
        v("Mario Math Tutoring","blmq6ms0_es","https://www.youtube.com/watch?v=blmq6ms0_es","Easy","Low","Fast","Fast"),
    ]),
    "2.3": ("Unit2", "Lesson2.3_Video.html", "Lesson2.3_Summary.html", [
        v("The Organic Chemistry Tutor","TCBu8PD4Lls","https://www.youtube.com/watch?v=TCBu8PD4Lls","Medium","Medium-High","Medium","Medium"),
        v("Khan Academy","Q5gk9ljVuTE","https://www.youtube.com/watch?v=Q5gk9ljVuTE","Medium","Medium-High","Medium","Medium"),
    ]),
    "2.4": ("Unit2", "Lesson2.4_Video.html", "Lesson2.4_Summary.html", [
        v("Khan Academy","GEId0GonOZM","https://www.youtube.com/watch?v=GEId0GonOZM","Medium-Easy","Medium","Fast","Fast"),
        v("Sri Chaitanya Academy NEET","yAjkQ1YqLEE","https://www.youtube.com/watch?v=yAjkQ1YqLEE","Medium","Medium-High","Medium","Medium"),
    ]),
    "2.5": ("Unit2", "Lesson2.5_Video.html", "Lesson2.5_Summary.html", [
        v("Erin Larson","36nALme6JLo","https://www.youtube.com/watch?v=36nALme6JLo","Medium","Medium-High","Medium","Medium"),
        v("The Organic Chemistry Tutor","eq1frp_ZyP8","https://www.youtube.com/watch?v=eq1frp_ZyP8","Medium","Medium-High","Medium","Medium"),
    ]),
    "2.6": ("Unit2", "Lesson2.6_Video.html", "Lesson2.6_Summary.html", [
        v("Acute Geometry class","sG5qn-HWBgI","https://www.youtube.com/watch?v=sG5qn-HWBgI&t=28s","Easy","Low","Very Fast","Fast","?start=28"),
        v("Math Professor Martin","Jrp8v1mxafI","https://www.youtube.com/watch?v=Jrp8v1mxafI","Medium","Medium-High","Medium-Fast","Medium"),
        v("Miacademy","ppw-ffPmmGo","https://www.youtube.com/watch?v=ppw-ffPmmGo","Medium-Hard","High","Long","Slow"),
    ]),
    "2.7": ("Unit2", "Lesson2.7_Video.html", "Lesson2.7_Summary.html", [
        v("The Organic Chemistry Tutor","cboityRIf4Q","https://www.youtube.com/watch?v=cboityRIf4Q","Easy","Medium","Fast","Medium"),
        v("Erin Larson","Yb_stoVRTes","https://www.youtube.com/watch?v=Yb_stoVRTes","Medium-Easy","Medium","Fast","Fast"),
    ]),
    "2.8": ("Unit2", "Lesson2.8_Video.html", "Lesson2.8_Summary.html", [
        v("Khan Academy","H-de6Tkxej8","https://www.youtube.com/watch?v=H-de6Tkxej8","Medium-Easy","Medium","Fast","Medium"),
        v("Professor Dave","dA94zyaLuhk","https://www.youtube.com/watch?v=dA94zyaLuhk","Medium","Medium-High","Medium-Fast","Medium"),
        v("The Organic Chemistry Tutor","e4o7X6LyX-I","https://www.youtube.com/watch?v=e4o7X6LyX-I","Easy","Medium-Low","Fast","Fast"),
        v("Khan Academy","kXcG6oYh3i8","https://www.youtube.com/watch?v=kXcG6oYh3i8&t=563s","Medium-Hard","High","Medium-Long","Slow","?start=563"),
    ]),
    "2.9": ("Unit2", "Lesson2.9_Video.html", "Lesson2.9_Summary.html", [
        v("Mario Math Tutoring","uKnE23jqgJc","https://www.youtube.com/watch?v=uKnE23jqgJc","Medium","Medium","Fast","Medium"),
        v("The Organic Chemistry Tutor","PXnAKcBipKM","https://www.youtube.com/watch?v=PXnAKcBipKM","Medium","Medium-High","Medium","Medium"),
    ]),
    "3.1": ("Unit3", "Lesson3.1_Video.html", "Lesson3.1_Summary.html", [
        v("Khan Academy","H-E5rlpCVu4","https://www.youtube.com/watch?v=H-E5rlpCVu4&t=1s","Medium-Easy","Medium","Medium-Fast","Medium","?start=1"),
        v("Your Math Tutor","DIyzTaotpR0","https://www.youtube.com/watch?v=DIyzTaotpR0","Medium","Medium-High","Medium-Fast","Medium"),
        v("Khan Academy","gRKZaojKeP0","https://www.youtube.com/watch?v=gRKZaojKeP0","Easy","Low","Fast","Fast"),
        v("Mario Math Tutoring","3Ex7SpsA9MI","https://www.youtube.com/watch?v=3Ex7SpsA9MI&t=10s","Medium-Hard","High","Long","Slow","?start=10"),
    ]),
    "3.2": ("Unit3", "Lesson3.2_Video.html", "Lesson3.2_Summary.html", [
        v("Cognito","I5auyoXYoX0","https://www.youtube.com/watch?v=I5auyoXYoX0&t=1s","Medium-Easy","Medium","Medium-Fast","Medium","?start=1"),
        v("Minity Math","5vgv3gLPXog","https://www.youtube.com/watch?v=5vgv3gLPXog","Medium","Medium-High","Medium-Fast","Medium"),
        v("Professor Dave","dA94zyaLuhk","https://www.youtube.com/watch?v=dA94zyaLuhk","Medium-Hard","High","Medium","Slow"),
        v("Beast Mode Maths","dxq4DootEOc","https://www.youtube.com/watch?v=dxq4DootEOc","Medium","Medium-High","Medium-Fast","Medium"),
    ]),
    "3.3": ("Unit3", "Lesson3.3_Video.html", "Lesson3.3_Summary.html", [
        v("Professor Dave Explains","lz8zVJxRFX8","https://www.youtube.com/watch?v=lz8zVJxRFX8","Easy","Low","Fast","Fast"),
        v("The Organic Chemistry Tutor","jlkE4VCnhdE","https://www.youtube.com/watch?v=jlkE4VCnhdE","Medium-Easy","Medium","Medium-Fast","Medium"),
        v("The Organic Chemistry Tutor","jvjZ4rnERmM","https://www.youtube.com/watch?v=jvjZ4rnERmM","Easy","Low","Fast","Fast"),
        v("Khan Academy","R948Tsyq4vA","https://www.youtube.com/watch?v=R948Tsyq4vA","Easy","Low","Fast","Fast"),
    ]),
    "3.4": ("Unit3", "Lesson3.4_Video.html", "Lesson3.4_Summary.html", [
        v("The Organic Chemistry Tutor","JaX_dIDUYBg","https://www.youtube.com/watch?v=JaX_dIDUYBg","Medium-Hard","High","Medium-Long","Slow"),
        v("The Organic Chemistry Tutor","LTb2-LE7StE","https://www.youtube.com/watch?v=LTb2-LE7StE","Easy","Low","Fast","Fast"),
        v("Cognito","ys0Dxj-jKTk","https://www.youtube.com/watch?v=ys0Dxj-jKTk","Medium-Hard","High","Medium-Long","Slow"),
        v("Khan Academy","gvwKv6F69F0","https://www.youtube.com/watch?v=gvwKv6F69F0","Medium-Hard","High","Medium-Long","Slow"),
    ]),
    "3.5": ("Unit3", "Lesson3.5_Video.html", "Lesson3.5_Summary.html", [
        v("Brian McLogan","dUTcNlLub7Q","https://www.youtube.com/watch?v=dUTcNlLub7Q","Easy","Low","Fast","Fast"),
        v("The Organic Chemistry Tutor","0eYzPVgylO8","https://www.youtube.com/watch?v=0eYzPVgylO8","Easy","Low","Fast","Fast"),
        v("Khan Academy","L1c0SP4W4ro","https://www.youtube.com/watch?v=L1c0SP4W4ro","Medium-Hard","High","Medium-Long","Slow"),
    ]),
    "3.6": ("Unit3", "Lesson3.6_Video.html", "Lesson3.6_Summary.html", [
        v("Khan Academy","iATjsfAX8yc","https://www.youtube.com/watch?v=iATjsfAX8yc","Medium","Medium-High","Medium-Fast","Medium"),
        v("Khan Academy","yj4oS-27Q3k","https://www.youtube.com/watch?v=yj4oS-27Q3k","Easy","Low","Fast","Fast"),
        v("Khan Academy","V0xounKGEXs","https://www.youtube.com/watch?v=V0xounKGEXs","Easy","Low","Fast","Fast"),
    ]),
    "3.7": ("Unit3", "Lesson3.7_Video.html", "Lesson3.7_Summary.html", [
        v("The Organic Chemistry Tutor","PXnAKcBipKM","https://www.youtube.com/watch?v=PXnAKcBipKM","Easy","Low","Fast","Fast"),
        v("Khan Academy","vsgrWDLEzcQ","https://www.youtube.com/watch?v=vsgrWDLEzcQ","Medium","Medium-High","Medium-Fast","Medium"),
        v("Khan Academy","pAlq9fFwtus","https://www.youtube.com/watch?v=pAlq9fFwtus","Easy","Low","Fast","Fast"),
        v("Mathtalka","Re0s1NPZ4ek","https://www.youtube.com/watch?v=Re0s1NPZ4ek","Medium","Medium-High","Medium-Fast","Medium"),
    ]),
    "4.1": ("Unit4", "Lesson4.1_Video.html", "Lesson4.1_Summary.html", [
        v("Cognito","NAxRP38GtzQ","https://www.youtube.com/watch?v=NAxRP38GtzQ&t=23s","Easy","Low","Fast","Fast","?start=23"),
        v("The Organic Chemistry Tutor","DdAwGinauoI","https://www.youtube.com/watch?v=DdAwGinauoI","Medium-Hard","High","Medium-Long","Slow"),
        v("Khan Academy","D5lZ3thuEeA","https://www.youtube.com/watch?v=D5lZ3thuEeA","Medium","Medium-High","Medium-Fast","Medium"),
        v("Khan Academy","uMcEgALdvgk","https://www.youtube.com/watch?v=uMcEgALdvgk","Medium","Medium-High","Medium-Fast","Medium"),
    ]),
    "4.2": ("Unit4", "Lesson4.2_Video.html", "Lesson4.2_Summary.html", [
        v("The Organic Chemistry Tutor","ndqxxAUDF5Y","https://www.youtube.com/watch?v=ndqxxAUDF5Y","Medium-Hard","High","Medium-Long","Slow"),
        v("The Organic Chemistry Tutor","4Dv5IFqATrc","https://www.youtube.com/watch?v=4Dv5IFqATrc","Medium-Hard","High","Medium-Long","Slow"),
        v("The Organic Chemistry Tutor","q7vI2oXL0gQ","https://www.youtube.com/watch?v=q7vI2oXL0gQ","Medium","Medium-High","Medium-Fast","Medium"),
        v("Khan Academy","7UISwx2Mr4c","https://www.youtube.com/watch?v=7UISwx2Mr4c","Easy","Low","Fast","Fast"),
    ]),
    "4.3": ("Unit4", "Lesson4.3_Video.html", "Lesson4.3_Summary.html", [
        v("Cognito","aK8i7LKZd9o","https://www.youtube.com/watch?v=aK8i7LKZd9o","Medium-Hard","High","Medium-Long","Slow"),
        v("Khan Academy","d5UCZ9hO8X4","https://www.youtube.com/watch?v=d5UCZ9hO8X4","Easy","Low","Fast","Fast"),
        v("The Organic Chemistry Tutor","jWHOF6cFbpw","https://www.youtube.com/watch?v=jWHOF6cFbpw","Easy","Low","Fast","Fast"),
        v("Mario Math Tutoring","lYIr2-kb-lE","https://www.youtube.com/watch?v=lYIr2-kb-lE","Medium-Hard","High","Medium-Long","Slow"),
    ]),
    "4.4": ("Unit4", "Lesson4.4_Video.html", "Lesson4.4_Summary.html", [
        v("The Organic Chemistry Tutor","YiFwvAFk-xs","https://www.youtube.com/watch?v=YiFwvAFk-xs","Medium","Medium-High","Medium-Fast","Medium"),
        v("Brian McLogan","_MhLzwjiGOM","https://www.youtube.com/watch?v=_MhLzwjiGOM","Medium","Medium-High","Medium-Fast","Medium"),
        v("Mario Math Tutoring","pi2V8pRCewE","https://www.youtube.com/watch?v=pi2V8pRCewE&t=192s","Medium-Hard","High","Medium-Long","Slow","?start=192"),
        v("Khan Academy","CJrVOf_3dN0","https://www.youtube.com/watch?v=CJrVOf_3dN0","Easy","Low","Fast","Fast"),
    ]),
    "4.5": ("Unit4", "Lesson4.5_Video.html", "Lesson4.5_Summary.html", [
        v("Yaymath","T23BbKHTH3o","https://www.youtube.com/watch?v=T23BbKHTH3o","Medium","Medium-High","Medium-Fast","Medium"),
        v("Mashup Math","DvCsRs6sSRQ","https://www.youtube.com/watch?v=DvCsRs6sSRQ","Medium-Hard","High","Medium-Long","Slow"),
        v("Khan Academy","5EX7tYQEB_M","https://www.youtube.com/watch?v=5EX7tYQEB_M","Easy","Low","Fast","Fast"),
    ]),
    "4.6": ("Unit4", "Lesson4.6_Video.html", "Lesson4.6_Summary.html", [
        v("Khan Academy","7FTNWE7RTfQ","https://www.youtube.com/watch?v=7FTNWE7RTfQ","Medium","Medium-High","Medium-Fast","Medium"),
        v("Chegg","in7LWBgKaAM","https://www.youtube.com/watch?v=in7LWBgKaAM","Medium","Medium-High","Medium-Fast","Medium"),
        v("The Organic Chemistry Tutor","6Yx923Ocoh4","https://www.youtube.com/watch?v=6Yx923Ocoh4","Medium-Hard","High","Medium-Long","Slow"),
        v("The Organic Chemistry Tutor","vIlWlauZV7E","https://www.youtube.com/watch?v=vIlWlauZV7E","Easy","Low","Fast","Fast"),
    ]),
    "4.7": ("Unit4", "Lesson4.7_Video.html", "Lesson4.7_Summary.html", [
        v("Khan Academy","Tn9U8hLu9aI","https://www.youtube.com/watch?v=Tn9U8hLu9aI","Medium","Medium-High","Medium-Fast","Medium"),
        v("The Organic Chemistry Tutor","GqHWdTLL8Qw","https://www.youtube.com/watch?v=GqHWdTLL8Qw","Medium-Hard","High","Medium-Long","Slow"),
        v("Khan Academy","3aDV3L8aZtY","https://www.youtube.com/watch?v=3aDV3L8aZtY","Medium","Medium-High","Medium-Fast","Medium"),
        v("Khan Academy","KZMRhWdzEPo","https://www.youtube.com/watch?v=KZMRhWdzEPo","Easy","Low","Fast","Fast"),
    ]),
    "4.8": ("Unit4", "Lesson4.8_Video.html", "Lesson4.8_Summary.html", [
        v("The Organic Chemistry Tutor","PXnAKcBipKM","https://www.youtube.com/watch?v=PXnAKcBipKM&t=69s","Medium-Hard","High","Medium-Long","Slow","?start=69"),
        v("Mario Math Tutoring","uKnE23jqgJc","https://www.youtube.com/watch?v=uKnE23jqgJc","Medium","Medium-High","Medium-Fast","Medium"),
        v("Mathermind","9ZdEs1jjIJ0","https://www.youtube.com/watch?v=9ZdEs1jjIJ0","Easy","Low","Fast","Fast"),
    ]),
    "5.1": ("Unit5", "Lesson5.1_Video.html", "Lesson5.1_Summary.html", [
        v("Khan Academy","PlY3e_-9JUA","https://www.youtube.com/watch?v=PlY3e_-9JUA","Medium-Hard","High","Medium-Long","Slow"),
        v("The Organic Chemistry Tutor","xyNBZuUjmSE","https://www.youtube.com/watch?v=xyNBZuUjmSE","Medium","Medium-High","Medium-Fast","Medium"),
        v("The Organic Chemistry Tutor","SyzkgBjXtIs","https://www.youtube.com/watch?v=SyzkgBjXtIs&t=183s","Easy","Low","Fast","Fast","?start=183"),
        v("Khan Academy","TpIBLnRAslI","https://www.youtube.com/watch?v=TpIBLnRAslI","Medium-Hard","High","Medium-Long","Slow"),
    ]),
    "5.2": ("Unit5", "Lesson5.2_Video.html", "Lesson5.2_Summary.html", [
        v("The Organic Chemistry Tutor","_JdkDR4R8E4","https://www.youtube.com/watch?v=_JdkDR4R8E4&t=1s","Medium","Medium-High","Medium-Fast","Medium","?start=1"),
        v("The Organic Chemistry Tutor","oJyTKVcE4iM","https://www.youtube.com/watch?v=oJyTKVcE4iM&t=2s","Easy","Low","Fast","Fast","?start=2"),
        v("Khan Academy","Xt4sT0fV9Pw","https://www.youtube.com/watch?v=Xt4sT0fV9Pw","Medium-Hard","High","Medium-Long","Slow"),
        v("Khan Academy","GiGLhXFBtRg","https://www.youtube.com/watch?v=GiGLhXFBtRg","Medium","Medium-High","Medium-Fast","Medium"),
    ]),
    "5.3": ("Unit5", "Lesson5.3_Video.html", "Lesson5.3_Summary.html", [
        v("Khan Academy","KlKYvbigBqs","https://www.youtube.com/watch?v=KlKYvbigBqs&t=99s","Easy","Low","Fast","Fast","?start=99"),
        v("Math with Mark","bV-u8QVxpRY","https://www.youtube.com/watch?v=bV-u8QVxpRY","Medium-Hard","High","Medium-Long","Slow"),
        v("Mario Math Tutoring","RZkOM7jWf7o","https://www.youtube.com/watch?v=RZkOM7jWf7o","Medium","Medium-High","Medium-Fast","Medium"),
        v("The Organic Chemistry Tutor","rfMZwrq-wL8","https://www.youtube.com/watch?v=rfMZwrq-wL8","Easy","Low","Fast","Fast"),
    ]),
    "5.4": ("Unit5", "Lesson5.4_Video.html", "Lesson5.4_Summary.html", [
        v("The Organic Chemistry Tutor","GawWGpnjy1c","https://www.youtube.com/watch?v=GawWGpnjy1c","Medium-Hard","High","Medium-Long","Slow"),
    ]),
    "5.5": ("Unit5", "Lesson5.5_Video.html", "Lesson5.5_Summary.html", [
        v("Mario Math Tutoring","RZkOM7jWf7o","https://www.youtube.com/watch?v=RZkOM7jWf7o","Medium","Medium-High","Medium-Fast","Medium"),
        v("Khan Academy","KlKYvbigBqs","https://www.youtube.com/watch?v=KlKYvbigBqs&t=100s","Easy","Low","Fast","Fast","?start=100"),
        v("Mario Math Tutoring","ePK-88DNsis","https://www.youtube.com/watch?v=ePK-88DNsis&t=40s","Medium-Hard","High","Medium-Long","Slow","?start=40"),
    ]),
    "5.6": ("Unit5", "Lesson5.6_Video.html", "Lesson5.6_Summary.html", [
        v("MarnellMathClass","nW0eOqpfrT0","https://www.youtube.com/watch?v=nW0eOqpfrT0","Medium","Medium-High","Medium-Fast","Medium"),
        v("iteachAlgebra","8ZZzY-mJMJs","https://www.youtube.com/watch?v=8ZZzY-mJMJs","Easy","Low","Fast","Fast"),
        v("Tarver Academy","hBFPsA46Q_g","https://www.youtube.com/watch?v=hBFPsA46Q_g","Medium-Hard","High","Medium-Long","Slow"),
    ]),
    "6.1": ("Unit6", "Lesson6.1_Video.html", "Lesson6.1_Summary.html", [
        v("1st Class Math","FZw0XTHA2Eo","https://www.youtube.com/watch?v=FZw0XTHA2Eo","Medium","Medium-High","Medium-Fast","Medium"),
        v("The Organic Chemistry Tutor","9_Y8P3oHwL0","https://www.youtube.com/watch?v=9_Y8P3oHwL0","Easy","Low","Fast","Fast"),
        v("The Organic Chemistry Tutor","OEzEo4XqzJQ","https://www.youtube.com/watch?v=OEzEo4XqzJQ","Medium-Hard","High","Medium-Long","Slow"),
        v("Khan Academy","qG3HnRccrQU","https://www.youtube.com/watch?v=qG3HnRccrQU","Medium","Medium-High","Medium-Fast","Medium"),
    ]),
    "6.2": ("Unit6", "Lesson6.2_Video.html", "Lesson6.2_Summary.html", [
        v("The Organic Chemistry Tutor","t42sLuns4Qs","https://www.youtube.com/watch?v=t42sLuns4Qs","Easy","Low","Fast","Fast"),
        v("The Organic Chemistry Tutor","LrwYAC_4ThY","https://www.youtube.com/watch?v=LrwYAC_4ThY","Medium-Hard","High","Medium-Long","Slow"),
        v("Khan Academy","Mep0foZMOCg","https://www.youtube.com/watch?v=Mep0foZMOCg","Medium","Medium-High","Medium-Fast","Medium"),
        v("The Organic Chemistry Tutor","k7iV42nkXc0","https://www.youtube.com/watch?v=k7iV42nkXc0","Easy","Low","Fast","Fast"),
    ]),
    "6.3": ("Unit6", "Lesson6.3_Video.html", "Lesson6.3_Summary.html", [
        v("Cahillmath","lk1iYTMW8Ko","https://www.youtube.com/watch?v=lk1iYTMW8Ko","Medium-Hard","High","Medium-Long","Slow"),
        v("iteachAlgebra","z3Q_1BXR_uQ","https://www.youtube.com/watch?v=z3Q_1BXR_uQ","Medium","Medium-High","Medium-Fast","Medium"),
        v("Nicole Hamilton","rHQ8WDaEnO4","https://www.youtube.com/watch?v=rHQ8WDaEnO4","Easy","Low","Fast","Fast"),
    ]),
    "6.4": ("Unit6", "Lesson6.4_Video.html", "Lesson6.4_Summary.html", [
        v("The Organic Chemistry Tutor","Ov4aTty67A8","https://www.youtube.com/watch?v=Ov4aTty67A8","Medium-Hard","High","Medium-Long","Slow"),
        v("Khan Academy","5CeBlu260Rw","https://www.youtube.com/watch?v=5CeBlu260Rw","Medium","Medium-High","Medium-Fast","Medium"),
        v("Khan Academy","Q3wfb0CPhIY","https://www.youtube.com/watch?v=Q3wfb0CPhIY","Easy","Low","Fast","Fast"),
    ]),
    "6.5": ("Unit6", "Lesson6.5_Video.html", "Lesson6.5_Summary.html", [
        v("The Organic Chemistry Tutor","uXo_Vpctmrg","https://www.youtube.com/watch?v=uXo_Vpctmrg","Medium-Hard","High","Medium-Long","Slow"),
        v("Cognito","mlG56WCfobI","https://www.youtube.com/watch?v=mlG56WCfobI","Medium","Medium-High","Medium-Fast","Medium"),
        v("The Organic Chemistry Tutor","ogcH3eM5beM","https://www.youtube.com/watch?v=ogcH3eM5beM","Easy","Low","Fast","Fast"),
    ]),
}


def make_video_item(vd):
    dcolor = dc(vd["diff"])
    detcolor = ec(vd["det"])
    scolor = sc(vd["spd"])
    pcolor = pc(vd["pace"])
    return (
        f'<div class="videos-panel-item">'
        f'<a data-color-detail="{detcolor}" data-color-difficulty="{dcolor}" data-color-pace="{pcolor}" data-color-speed="{scolor}"'
        f' data-rating-detail="{vd["det"]}" data-rating-difficulty="{vd["diff"]}" data-rating-pace="{vd["pace"]}" data-rating-speed="{vd["spd"]}"'
        f' data-video-id="{vd["id"]}" data-video-src="{vd["embed"]}" data-video-title="{vd["channel"]}"'
        f' href="{vd["watch"]}">{vd["channel"]}</a>'
        f'<div aria-hidden="true" class="mini-rubric">'
        f'<span style="background:{dcolor}"></span>'
        f'<span style="background:{detcolor}"></span>'
        f'<span style="background:{scolor}"></span>'
        f'<span style="background:{pcolor}"></span>'
        f'</div></div>'
    )


# Patterns to search for in each file
IFRAME_PLACEHOLDER = '                        <div class="video-embed">\n                            <!-- Video iframe placeholder causing empty box initially -->\n                        </div>'

def make_iframe(primary):
    return (
        '                        <div class="video-embed">\n'
        f'                            <iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen="" referrerpolicy="strict-origin-when-cross-origin" src="{primary["embed"]}" title="{primary["channel"]} Video"></iframe>\n'
        '                        </div>'
    )


# The rubric-box block (same in all files) — we find it via a regex
RUBRIC_BOX_PATTERN = re.compile(
    r'<div class="rubric-box">.*?</div>\s*</div>\s*</div>\s*</div>',
    re.DOTALL
)

# The videos-panel placeholder pattern (varies by lesson number)
def videos_panel_pattern(lesson_num):
    return re.compile(
        r'<div class="videos-panel" aria-hidden="true">\s*'
        r'<div class="videos-panel-title">Lesson ' + re.escape(lesson_num) + r' videos</div>\s*'
        r'<div class="videos-panel-item">.*?</div>\s*</div>\s*</div>',
        re.DOTALL
    )


def make_videos_panel(lesson_num, videos):
    items = "".join(make_video_item(vd) for vd in videos)
    return (
        f'<div class="videos-panel" aria-hidden="true">'
        f'<div class="videos-panel-title">Lesson {lesson_num} videos</div>'
        f'{items}'
        f'</div>'
    )


def make_rubric_data(primary):
    dcolor = dc(primary["diff"])
    detcolor = ec(primary["det"])
    scolor = sc(primary["spd"])
    pcolor = pc(primary["pace"])
    return (
        f'<div class="rubric-data" data-difficulty="{primary["diff"]}" data-difficulty-color="{dcolor}"'
        f' data-detail="{primary["det"]}" data-detail-color="{detcolor}"'
        f' data-speed="{primary["spd"]}" data-speed-color="{scolor}"'
        f' data-pace="{primary["pace"]}" data-pace-color="{pcolor}"></div>'
    )


updated = []
errors = []

for lesson_num, (unit_dir, filename, summary_file, videos) in LESSONS.items():
    filepath = os.path.join(BASE, unit_dir, filename)
    if not os.path.exists(filepath):
        errors.append(f"FILE NOT FOUND: {filepath}")
        continue

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    primary = videos[0]

    # 1. Replace iframe placeholder
    new_iframe = make_iframe(primary)
    if IFRAME_PLACEHOLDER in content:
        content = content.replace(IFRAME_PLACEHOLDER, new_iframe, 1)
    else:
        errors.append(f"IFRAME PLACEHOLDER NOT FOUND in Lesson {lesson_num}")

    # 2. Replace videos-panel
    panel_re = videos_panel_pattern(lesson_num)
    new_panel = make_videos_panel(lesson_num, videos)
    new_content, n = panel_re.subn(new_panel, content, count=1)
    if n == 0:
        errors.append(f"VIDEOS PANEL NOT FOUND in Lesson {lesson_num}")
    else:
        content = new_content

    # 3. Replace rubric-box with rubric-data
    new_rubric = make_rubric_data(primary)
    new_content, n = RUBRIC_BOX_PATTERN.subn(new_rubric, content, count=1)
    if n == 0:
        errors.append(f"RUBRIC BOX NOT FOUND in Lesson {lesson_num}")
    else:
        content = new_content

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    updated.append(f"Lesson {lesson_num}: {filename}")

print(f"\nUpdated {len(updated)} files:")
for u in updated:
    print(f"  OK  {u}")

if errors:
    print(f"\nErrors ({len(errors)}):")
    for e in errors:
        print(f"  ERR  {e}")
else:
    print("\nNo errors.")
