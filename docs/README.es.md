# Autonomous Company

[English — fuente canónica](../README.md) · [Português](README.pt-BR.md)

Workspace de agentes para operaciones por empresa en Versat ERP, con instrucciones, skill importada, enrutamiento local privado y validación offline. No instala un servicio ni ejecuta transacciones por sí solo.

Responsable: **versat-open-source**; mantenedor: **@elviszoz**. Perfil: **agent / finance**, criticidad operativa alta. Gobernanza fijada en la revisión **9260d3a** de Versat AI Harness (VERSION **0.2.0**, cambios todavía en Unreleased), con commit completo y hashes en `.versat/`. Consulte la [decisión de adopción](decisions/0002-consumer-agent-layout.md).

Use Python **3.12.14** y ejecute en la raíz:

```sh
python3.12 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
cp versat-companies.example.json versat-companies.local.json
bash scripts/validate/run.sh
```

Complete el JSON local con sus empresas y los nombres exactos de conexiones MCP ya configuradas en el cliente. Los tokens permanecen en la configuración segura del cliente. Git ignora el archivo local; nunca fuerce su inclusión.

Abra el workspace en un cliente que lea `AGENTS.md` y `.agents/skills/`. Siga el [flujo operativo](../workflows/versat-operation/workflow.md): contexto ambiguo, configuración ausente, conexión no disponible o escritura no autorizada impiden llamadas.

Las Skills están en `.agents/skills/`; el operador supervisado se define en `.codex/agents/operator.toml`. Los workflows usan `workflows/<nombre>/workflow.md` y se cargan explícitamente. La carga nativa del operador requiere un cliente Codex compatible y verificación separada; no se instala ningún planificador. Consulte la [arquitectura de agentes y los requisitos de ejecución](architecture/agent-project.md).

La validación cubre estilo, pruebas, 15 escenarios ficticios, estructura de artefactos y vínculos de dependencias, esquemas, integridad de Standards y exclusión de datos privados. No certifica descubrimiento nativo de agentes, comportamiento del modelo ni conectividad real con el ERP.

Los cambios materiales siguen [SDD](../.versat/sdd/process.md), PR, revisión de CODEOWNERS y check `validate`. Consulte [contribuciones](../CONTRIBUTING.md), [arquitectura](architecture/overview.md), [operaciones](operations.md), [seguridad](../SECURITY.md) y [preparación](readiness.md).

No se ha elegido una licencia general de distribución. La publicación no concede una licencia de software; consulte la [procedencia](../THIRD_PARTY_NOTICES.md).
