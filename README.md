# hha

Lightweight skills for planning, building, and verifying.

## SK하이닉스 AI 해커톤 2026 본선 진출

**hha 하네스를 사용해 [SK하이닉스 AI 해커톤 2026](https://skhynix-hackathon.com/ai-2026) 본선에 진출했습니다.** 온라인 예선은 AI 파트너 크래프톤의 **COFA(Cofa-Probe)** 플랫폼에서 진행됐습니다.

hha는 [hhmode](https://github.com/unhaeos/hhmode)를 제한된 과제 환경에 맞게 간소화한 버전입니다.

README를 읽고, 필요한 질문을 함께 정리하고, 체크리스트형 SPEC을 만든 뒤 실제 결과로 검증합니다. 코드가 없는 프로젝트에서도 시작할 수 있습니다. 프로젝트의 AGENTS.md와 자동 인식 스킬로 사용하며 API 키, 플러그인, 전역 설정 변경이 필요하지 않습니다.

## 바로 시작

작업 환경에서 허용된 위치에 이 저장소를 가져옵니다. 아래 명령은 **과제 프로젝트 폴더에서**, 아직 `hha`라는 하위 폴더가 없을 때 실행합니다.

```sh
git clone --depth 1 https://github.com/unhaeos/hha.git hha
```

작업 공간 바깥에도 쓸 수 있다면 프로젝트 옆에 별도로 clone해도 됩니다. 그 경우 아래 요청의 `hha/`를 실제 경로로 바꿉니다. 기존 폴더는 덮어쓰지 않습니다.

프로젝트 폴더에서 설치합니다. Python 3.9 이상이 필요하며 패키지 설치는 없습니다.

```sh
python3 hha/scripts/install.py .
```

Windows 등에서 명령 이름이 `python`이면 `python hha/scripts/install.py .`를 사용합니다. 기본 설치 위치는 현재 공식 문서의 `.agents/skills/`입니다. `.codex/skills/`를 읽는 환경에서는 **대신** `python3 hha/scripts/install.py . --layout codex`를 사용하세요. 두 위치에 중복 설치할 필요는 없습니다. [공식 스킬 경로 안내](https://learn.chatgpt.com/docs/build-skills)

```text
project/
  AGENTS.md                 # 기존 지침을 보존하고 hha 참조만 추가
  .agents/skills/hha-*/      # Codex가 발견하는 스킬 (codex 옵션은 .codex/skills)
  .hha/                     # 지침과 스킬이 참조하는 리소스
  hha/                      # 다운로드한 원본
  hha-work/                 # 작업하면서 생성되는 SPEC과 검증 기록
  ...                       # 실제 프로젝트 소스
```

설치 스크립트는 같은 파일로 재실행할 수 있고, 다른 내용이 이미 있으면 덮어쓰지 않고 중단합니다. 업데이트 때 충돌하면 기존 사용자 변경을 먼저 확인하세요. Git 저장소나 커밋은 설치·구현·검증의 필수조건이 아닙니다.

로컬 Git이 가능하면 구현 전에 `git status --short --branch`와 `git log -1 --oneline`을 확인합니다. 초기 커밋이 없다면 원본 과제 파일을 검토해 명시적인 경로만 stage하고 로컬 baseline commit을 만드세요. `git add .`로 `hha/`, 설치 파일, 로컬 환경 파일이나 비밀 값을 함께 넣지 않습니다. 이후 작동하는 작은 단위마다 로컬 커밋을 남기되 push하지 않습니다. 한 checkout에서는 한 세션만 파일을 수정하고, 두 번째 세션은 안정된 커밋을 읽기 전용으로 검토합니다.

프로젝트 폴더에서 Codex를 시작해 `/skills` 또는 `$` 목록에 `hha-plan`, `hha-create-verification`, `hha-debug`, `hha-review`, `hha-ui`, `hha-writing`이 보이는지 확인합니다. 목록이 갱신되지 않으면 Codex를 재시작합니다. 제공 환경에서 다른 경로를 사용한다면 확인된 경로를 선택하세요.

그다음 요청하세요.

```text
AGENTS.md를 따르고 hha-plan으로 시작해줘.
프로젝트의 README와 기존 코드부터 확인하고, hha 자체는 작업 대상에서 제외해.
중요한 결정만 짧게 인터뷰한 뒤 체크리스트형 SPEC을 만들어줘.
README와 SPEC을 기준으로 프로젝트 전용 검증 스킬도 만들어줘.
코드가 없으면 검증 초안부터 만들고 최소 구현 후 실행 절차를 확정해.
이어서 구현하고 검증해줘. 화면이 필요하면 hha-ui를 함께 적용해.
추가 세션이나 서브에이전트를 쓸 수 있으면 한 명만 파일을 수정하고, 나머지는 안정된 로컬 커밋을 hha-review로 읽기 전용 검토해.
외부 전송, push, PR, 자동 제출, 전역 설정 변경은 하지 마.
```

계획까지만 원하면 마지막에 `이번에는 계획과 검증 초안까지만 작성해줘`라고 덧붙입니다. Python이 없거나 프로젝트 스킬 등록이 지원되지 않으면 설치 대신 `hha/AGENTS.md를 읽고 적용해줘`라고 요청할 수 있습니다. 설치는 스킬 발견을 돕는 것이며 도구 권한이나 실행 능력을 추가하지 않습니다.

## 구성

| 파일 | 역할 |
|---|---|
| [AGENTS.md](AGENTS.md) | 작업 시작, 단계 전환, 제한된 환경의 기본 규칙 |
| [hha-plan](skills/hha-plan/SKILL.md) | 필요한 인터뷰와 체크리스트형 SPEC |
| [hha-create-verification](skills/hha-create-verification/SKILL.md) | 요구사항별 검증 스킬 생성 및 갱신 |
| [hha-debug](skills/hha-debug/SKILL.md) | 재현, 원인, 수정, 재검증 |
| [hha-review](skills/hha-review/SKILL.md) | 새 컨텍스트의 읽기 전용 요구사항·코드 리뷰 |
| [hha-ui](skills/hha-ui/SKILL.md) | 읽기 쉬운 화면, 구체적인 문구, 절제된 시각 구조 |
| [hha-writing](skills/hha-writing/SKILL.md) | 버튼 한 줄부터 문서까지 구체적인 문구와 설명 |
| [검증 기록](docs/validation.md) | 이 저장소에서 실제 확인한 범위와 한계 |

기본 산출물은 **프로젝트 쪽** `hha-work/SPEC.md`, `hha-work/verification/SKILL.md`, `hha-work/verification/features.md`, `hha-work/evidence/`입니다. `hha-work`가 이미 있다면 먼저 읽고 이어 쓰거나 별도 경로를 정합니다. 공식 제출 파일명은 과제 안내가 우선하며 이 파일들을 무조건 제출하지 않습니다.

다음 세션에서는 `AGENTS.md와 hha-work/SPEC.md, hha-work/verification/SKILL.md를 읽고 남은 작업부터 이어가줘`라고 요청합니다. 과거 검증 후 관련 코드나 조건이 바뀌었다면 다시 확인합니다.

## 제한된 작업 환경

환경 운영 지침과 프로젝트 지침을 우선합니다. 하네스는 모델 업데이트, 다른 AI 연결, 개인 인증, 자동 동기화, 외부 로그 전송, 브라우저 조작이나 MCP 연결을 기본으로 요구하지 않습니다. 과제를 읽은 뒤 MCP가 필요한 경우에는 필요한 기능, 외부로 나가는 데이터, 인증과 설정 변경, 연결 실패 시 대안을 먼저 확인합니다. 허용 여부가 불명확하면 연결하지 않습니다. 허용 여부가 확인되지 않은 UI 자동화는 사용하지 않고 해당 검증을 미실행으로 남깁니다. AI 사용이 허용되지 않는 단계로 전환되면 작업을 중단합니다.

하네스 실행 중 push/PR/머지는 없습니다. 이 공개 저장소를 유지보수하는 일과, 가져간 환경에서 프로젝트를 작업하는 일은 별개입니다. 공개 자료 유지 기간이 정해진 환경에서 사용한다면 그 기간 동안 저장소를 공개 상태로 유지해야 합니다.

## 제거

프로젝트 AGENTS.md에서 `hha:start`부터 `hha:end`까지의 블록만 제거하고, 설치한 경로의 `hha-*` 스킬 폴더와 `.hha/`를 제거합니다. 다른 스킬이나 기존 지침은 보존하세요. 다운로드한 `hha/`도 필요 없으면 제거할 수 있습니다. `hha-work/`에는 계획과 증거가 있으므로 별도로 보존 여부를 결정하세요. 전역 스킬 디렉터리, Git hooks, 모델 설정은 수정하지 않습니다.

## 출처

pstack의 프로젝트별 검증 스킬 생성 방식을 단일 세션, 문서 우선, 빈 프로젝트 시작에 맞춰 조정했습니다. UI 지침은 사용자의 구체적 선호와 frontend-design의 일부 설계 원칙을 반영했습니다. [출처와 라이선스](THIRD_PARTY.md)를 참고하세요.
