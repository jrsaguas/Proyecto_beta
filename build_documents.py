from pathlib import Path
from docx import Document
from docx.shared import Pt
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

ROOT = Path(__file__).parent
md = (ROOT / "investigacion_ia_agentiva.md").read_text(encoding="utf-8")

# DOCX
doc = Document()
styles = doc.styles
styles["Normal"].font.name = "Aptos"
styles["Normal"].font.size = Pt(10.5)
doc.add_heading("Inteligencia Artificial Agentiva", 0)
doc.add_paragraph("Informe de investigación · 29 de septiembre de 2026")
doc.add_paragraph("Fundamentos, arquitectura, herramientas, memoria, planificación, multiagente, seguridad y ecosistema open source.")
doc.add_heading("Conceptos clave", 1)
for item in [
    "Agente: sistema que puede decidir y actuar dentro de un objetivo y restricciones.",
    "Tool calling: selección e invocación estructurada de herramientas.",
    "Estado: información de la ejecución actual.",
    "Memoria: persistencia de información relevante entre pasos o sesiones.",
    "RAG: recuperación de conocimiento externo para aportar contexto.",
    "Orquestación: control del ciclo, herramientas, handoffs, errores y terminación.",
    "Guardrails: restricciones técnicas y políticas sobre entradas, salidas y acciones.",
    "Observabilidad: trazas, métricas y registros para depuración y evaluación."
]:
    doc.add_paragraph(item, style="List Bullet")
doc.add_heading("Arquitectura de referencia", 1)
doc.add_paragraph("Objetivo → observar → interpretar → planear → validar permisos → ejecutar herramienta → observar resultado → evaluar → repetir o terminar.")
doc.add_heading("Frameworks y plataformas", 1)
for item in [
    "OpenAI Agents SDK — code-first, tools, handoffs, guardrails y estado.",
    "Microsoft Agent Framework — agentes, workflows, memoria, RAG, herramientas y seguridad.",
    "Google ADK — agentes y sistemas multiagente.",
    "LangGraph — orquestación stateful y agentes de larga duración.",
    "CrewAI — equipos de agentes y tareas.",
    "AutoGen — multiagente; en 2026 está en maintenance mode.",
    "LlamaIndex / Haystack — datos, RAG, workflows y agentes.",
    "Dify / Flowise — construcción visual y autoalojamiento.",
    "OpenHands — agentes para desarrollo de software.",
    "Browser Use — agentes que interactúan con navegadores."
]:
    doc.add_paragraph(item, style="List Bullet")
doc.add_heading("Seguridad", 1)
doc.add_paragraph("Los riesgos incluyen prompt injection, abuso de herramientas, privilegios excesivos, exfiltración, credenciales expuestas, memoria contaminada y falta de trazabilidad. Controles recomendados: mínimo privilegio, validación de argumentos, sandboxing, aprobación humana, límites de presupuesto, observabilidad y pruebas adversariales.")
doc.add_heading("Evaluación", 1)
doc.add_paragraph("Medir éxito de tarea, exactitud, éxito de herramientas, recuperación ante errores, latencia, costo, número de pasos, tokens, procedencia, acciones no autorizadas y robustez adversarial.")
doc.add_heading("Fuentes", 1)
for url in [
    "https://www.nist.gov/news-events/news/2026/02/announcing-ai-agent-standards-initiative-interoperable-and-secure",
    "https://developers.openai.com/api/docs/guides/agents/sdk",
    "https://learn.microsoft.com/en-us/agent-framework",
    "https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/",
    "https://github.com/langchain-ai/langgraph",
    "https://github.com/crewAIInc/crewAI",
    "https://github.com/microsoft/autogen",
    "https://github.com/google/adk-python",
    "https://github.com/langgenius/dify",
    "https://github.com/All-Hands-AI/OpenHands",
    "https://github.com/browser-use/browser-use"
]:
    doc.add_paragraph(url)
doc.save(ROOT / "informe_ia_agentiva.docx")

# XLSX
wb = Workbook()
ws = wb.active
ws.title = "Comparativa"
headers = ["Framework / plataforma","Categoría","Open source","Self-hosted","Modelo/API aparte","Tools","Memoria","Multiagente","RAG","Enfoque","Estado 2026","URL"]
rows = [
["OpenAI Agents SDK","SDK","Sí","Sí","Sí","Sí","Sí","Sí","Sí","Code-first","Activo","https://developers.openai.com/api/docs/guides/agents/sdk"],
["Microsoft Agent Framework","SDK","Sí","Sí","Sí","Sí","Sí","Sí","Sí","Agentes + workflows","Activo","https://learn.microsoft.com/en-us/agent-framework"],
["Google ADK","SDK","Sí","Sí","Sí","Sí","Sí","Sí","Sí","Agentes/multiagente","Activo","https://github.com/google/adk-python"],
["LangGraph","Orquestación","Sí","Sí","Sí","Sí","Sí","Sí","Sí","Stateful/long-running","Activo","https://github.com/langchain-ai/langgraph"],
["CrewAI","Framework","Sí","Sí","Sí","Sí","Sí","Sí","Sí","Teams/workflows","Activo","https://github.com/crewAIInc/crewAI"],
["AutoGen","Multiagente","Sí","Sí","Sí","Sí","Sí","Sí","Sí","Multiagente","Maintenance mode","https://github.com/microsoft/autogen"],
["LlamaIndex","Datos/agents","Sí","Sí","Sí","Sí","Sí","Sí","Sí","Datos/RAG/workflows","Activo","https://github.com/run-llama/llama_index"],
["Haystack","Framework","Sí","Sí","Sí","Sí","Sí","Sí","Sí","Pipelines/RAG","Activo","https://github.com/deepset-ai/haystack"],
["Semantic Kernel","SDK","Sí","Sí","Sí","Sí","Sí","Sí","Sí","Plugins/agentes","Activo","https://github.com/microsoft/semantic-kernel"],
["Dify","Plataforma visual","Sí","Sí","Sí","Sí","Sí","Sí","Sí","Visual/workflows","Activo","https://github.com/langgenius/dify"],
["Flowise","Plataforma visual","Sí","Sí","Sí","Sí","Sí","Sí","Sí","Visual/LLM apps","Activo","https://github.com/FlowiseAI/Flowise"],
["OpenHands","Agente de software","Sí","Sí","Sí","Sí","Sí","Sí","Sí","Coding agents","Activo","https://github.com/All-Hands-AI/OpenHands"],
["Browser Use","Browser agent","Sí","Sí","Sí","Sí","Sí","Sí","Parcial","Web automation","Activo","https://github.com/browser-use/browser-use"]
]
ws.append(headers)
for row in rows: ws.append(row)
for cell in ws[1]:
    cell.font = Font(bold=True)
    cell.fill = PatternFill("solid", fgColor="1F4E78")
    cell.font = Font(bold=True, color="FFFFFF")
    cell.alignment = Alignment(wrap_text=True)
ws.freeze_panes = "A2"
ws.auto_filter.ref = ws.dimensions
for i,w in enumerate([25,18,13,13,18,12,12,14,12,25,18,55],1):
    ws.column_dimensions[get_column_letter(i)].width = w

ws2 = wb.create_sheet("Criterios")
criteria = [
["Criterio","Qué revisar"],
["Open source","Licencia y disponibilidad del código."],
["Self-hosted","Posibilidad de ejecutar el runtime en infraestructura propia."],
["Free tier","Cuotas gratuitas del proveedor; pueden cambiar."],
["Modelo local","Posibilidad de conectar modelos ejecutados localmente."],
["Tools","Funciones, APIs, navegadores, archivos y MCP."],
["Memoria","Estado de sesión y persistencia."],
["Multiagente","Coordinación, handoffs o equipos."],
["RAG","Recuperación y uso de conocimiento externo."],
["Seguridad","Permisos, guardrails, aislamiento y observabilidad."]
]
for row in criteria: ws2.append(row)
ws2.column_dimensions["A"].width=22; ws2.column_dimensions["B"].width=90
for c in ws2[1]: c.font=Font(bold=True)
ws3 = wb.create_sheet("Fuentes")
sources = [
["Fuente","URL","Uso"],
["NIST AI Agent Standards Initiative","https://www.nist.gov/news-events/news/2026/02/announcing-ai-agent-standards-initiative-interoperable-and-secure","Estándares e interoperabilidad"],
["OpenAI Agents SDK","https://developers.openai.com/api/docs/guides/agents/sdk","SDK oficial"],
["Microsoft Agent Framework","https://learn.microsoft.com/en-us/agent-framework","Framework oficial"],
["OWASP Agentic Applications 2026","https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/","Seguridad"],
["Anthropic Building Effective Agents","https://www.anthropic.com/research/building-effective-agents","Patrones de agentes"],
["LangGraph","https://github.com/langchain-ai/langgraph","Framework"],
["CrewAI","https://github.com/crewAIInc/crewAI","Framework"],
["AutoGen","https://github.com/microsoft/autogen","Estado del proyecto"],
["Browser Use","https://github.com/browser-use/browser-use","Browser agents"]
]
for row in sources: ws3.append(row)
ws3.column_dimensions["A"].width=32; ws3.column_dimensions["B"].width=90; ws3.column_dimensions["C"].width=32
for c in ws3[1]: c.font=Font(bold=True)
wb.save(ROOT / "comparativa_ia_agentiva.xlsx")
print("Generados DOCX y XLSX")
