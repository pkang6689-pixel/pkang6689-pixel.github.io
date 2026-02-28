$files = @{
    "ArisEdu Project Folder\scripts\global_translations.js" = @(34282, 34247, 35161, 35233)
    "ArisEdu Project Folder\scripts\spanish_translations.js" = @(31338, 32086, 32121, 33070, 33749, 34059, 34060)
    "ArisEdu Project Folder\scripts\hindi_translations.js" = @(31239, 31987, 32022, 32971, 33650, 33960, 33961)
}

foreach ($filepath in $files.Keys) {
    Write-Host "Processing $filepath..."
    $lines = @(Get-Content -Path $filepath -Encoding UTF8)
    $fixed = 0
    
    foreach ($lineNo in ($files[$filepath] | Sort-Object -Descending)) {
        $idx = $lineNo - 1
        if ($idx -lt $lines.Count) {
            $line = $lines[$idx]
            if ($line -match '"\s*$' -and $line -notmatch '",\s*$') {
                $lines[$idx] = $line.TrimEnd() + ','
                $fixed++
                Write-Host "  Fixed line $lineNo"
            }
        }
    }
    
    $lines | Set-Content -Path $filepath -Encoding UTF8 -NoNewline
    Write-Host "  ✓ Fixed $fixed lines`n"
}

Write-Host "✓ All files fixed!"
