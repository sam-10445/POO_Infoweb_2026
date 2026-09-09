# SOLUÇÃO — EXERCÍCIO COMPLETO

Este exercício combina os padrões:

NOVO CADASTRO
+
NOVO ATRIBUTO
+
ASSOCIAÇÃO
+
ALTERAÇÃO DO SERVICE
+
ALTERAÇÃO DA UI
+
ALTERAÇÃO DO INDEX

Use nesta ordem:

1. `01_NOVO_CADASTRO`
2. `03_NOVO_ATRIBUTO`
3. `02_NOVA_ASSOCIACAO`

Não tente fazer tudo simultaneamente.

---

## ORDEM DOS ARQUIVOS

### Criar

Projeto/models/profissional.py

Projeto/models/profissionaldao.py

Projeto/templates/manterprofissionalui.py

---

### Alterar

Projeto/service.py

Projeto/index.py

Projeto/models/horario.py

Projeto/templates/manterhorarioui.py

---

## ORDEM DE IMPLEMENTAÇÃO

Profissional
↓
ProfissionalDAO
↓
Service
↓
ManterProfissionalUI
↓
IndexUI
↓
id_profissional em Horario
↓
Service de Horario
↓
ManterHorarioUI
↓
Teste