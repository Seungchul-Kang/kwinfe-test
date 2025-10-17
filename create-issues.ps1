# GitHub Issues 생성 스크립트
# 사용법: 먼저 GitHub Personal Access Token을 환경 변수로 설정해야 합니다.
# $env:GITHUB_TOKEN = "your_token_here"
# 그 후 이 스크립트를 실행: .\create-issues.ps1

$owner = "Seungchul-Kang"
$repo = "kwinfe-test"
$token = $env:GITHUB_TOKEN

if (-not $token) {
    Write-Host "오류: GITHUB_TOKEN 환경 변수가 설정되지 않았습니다." -ForegroundColor Red
    Write-Host "다음 명령으로 토큰을 설정하세요:" -ForegroundColor Yellow
    Write-Host '$env:GITHUB_TOKEN = "your_personal_access_token"' -ForegroundColor Yellow
    Write-Host ""
    Write-Host "GitHub Personal Access Token 생성 방법:" -ForegroundColor Cyan
    Write-Host "1. https://github.com/settings/tokens 접속" -ForegroundColor White
    Write-Host "2. 'Generate new token (classic)' 클릭" -ForegroundColor White
    Write-Host "3. 'repo' 권한 체크" -ForegroundColor White
    Write-Host "4. 생성된 토큰 복사" -ForegroundColor White
    exit 1
}

$headers = @{
    "Authorization" = "token $token"
    "Accept" = "application/vnd.github.v3+json"
}

$issueFiles = @(
    @{
        file = "phase1-project-setup.md"
        title = "Phase 1: 프로젝트 초기 설정"
        labels = @("setup", "phase-1", "priority-high")
    },
    @{
        file = "phase2-django-apps.md"
        title = "Phase 2: Django 앱 생성 및 설정"
        labels = @("feature", "phase-2", "priority-high")
    },
    @{
        file = "phase3-database-setup.md"
        title = "Phase 3: 데이터베이스 설정"
        labels = @("database", "phase-3", "priority-high")
    },
    @{
        file = "phase4-url-routing.md"
        title = "Phase 4: URL 라우팅 설정"
        labels = @("configuration", "phase-4", "priority-medium")
    },
    @{
        file = "phase5-template-development.md"
        title = "Phase 5: 템플릿 개발"
        labels = @("frontend", "templates", "phase-5", "priority-high")
    },
    @{
        file = "phase6-views-logic.md"
        title = "Phase 6: Views 및 로직 구현"
        labels = @("backend", "views", "phase-6", "priority-high")
    },
    @{
        file = "phase7-static-files.md"
        title = "Phase 7: 정적 파일 및 스타일링"
        labels = @("frontend", "css", "javascript", "phase-7", "priority-medium")
    },
    @{
        file = "phase8-security.md"
        title = "Phase 8: 보안 및 인증 강화"
        labels = @("security", "phase-8", "priority-high")
    },
    @{
        file = "phase9-testing.md"
        title = "Phase 9: 테스트 작성"
        labels = @("testing", "phase-9", "priority-high")
    },
    @{
        file = "phase10-documentation.md"
        title = "Phase 10: 문서화 및 배포 준비"
        labels = @("documentation", "phase-10", "priority-medium")
    }
)

Write-Host "GitHub Issues 생성 시작..." -ForegroundColor Green
Write-Host "저장소: $owner/$repo" -ForegroundColor Cyan
Write-Host ""

foreach ($issue in $issueFiles) {
    $filePath = "docs\issues\$($issue.file)"
    
    if (Test-Path $filePath) {
        $body = Get-Content $filePath -Raw -Encoding UTF8
        
        $issueData = @{
            title = $issue.title
            body = $body
            labels = $issue.labels
        } | ConvertTo-Json -Depth 10
        
        try {
            $response = Invoke-RestMethod -Uri "https://api.github.com/repos/$owner/$repo/issues" `
                -Method Post `
                -Headers $headers `
                -Body $issueData `
                -ContentType "application/json; charset=utf-8"
            
            Write-Host "✓ 이슈 생성 완료: $($issue.title)" -ForegroundColor Green
            Write-Host "  URL: $($response.html_url)" -ForegroundColor Gray
        }
        catch {
            Write-Host "✗ 이슈 생성 실패: $($issue.title)" -ForegroundColor Red
            Write-Host "  오류: $($_.Exception.Message)" -ForegroundColor Red
        }
        
        Start-Sleep -Milliseconds 500  # API Rate Limit 방지
    }
    else {
        Write-Host "✗ 파일을 찾을 수 없음: $filePath" -ForegroundColor Red
    }
}

Write-Host ""
Write-Host "완료! GitHub Issues 페이지를 확인하세요:" -ForegroundColor Green
Write-Host "https://github.com/$owner/$repo/issues" -ForegroundColor Cyan
