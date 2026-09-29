# Investigación completa: Inteligencia Artificial Agentiva

**Fecha de corte:** 29 de septiembre de 2026

## 1. Resumen ejecutivo

La IA agentiva describe sistemas que no se limitan a producir una respuesta a una instrucción aislada, sino que pueden mantener estado, seleccionar o invocar herramientas, ejecutar acciones, observar resultados y repetir ciclos hasta alcanzar un objetivo dentro de límites definidos. El elemento central no es simplemente usar un modelo grande, sino construir un sistema de ejecución alrededor del modelo.

Una arquitectura agentiva típica integra modelo de lenguaje o multimodal, instrucciones, estado/contexto, memoria, herramientas, orquestación, ejecución, observabilidad, evaluación y controles de seguridad. Los agentes pueden ser individuales o cooperar mediante arquitecturas multiagente.

NIST lanzó en febrero de 2026 su AI Agent Standards Initiative con énfasis en seguridad, interoperabilidad y estándares para agentes. OWASP publicó su Top 10 for Agentic Applications 2026 para riesgos específicos de sistemas que pueden planear y actuar sobre sistemas externos.

## 2. ¿Qué es la IA agentiva?

Un LLM tradicional transforma entradas lingüísticas en salidas. Un agente añade un bucle de decisión y ejecución. Una abstracción útil es:

Objetivo → observar contexto → razonar/decidir → seleccionar acción → ejecutar herramienta → observar resultado → evaluar → actualizar estado → repetir o terminar.

La agentividad es una propiedad del sistema completo y de su capacidad de actuar, no una propiedad exclusiva del modelo.

### 2.1 LLM, chatbot, workflow y agente

| Sistema | Característica principal |
|---|---|
| LLM | Genera contenido a partir de contexto. |
| Chatbot | Interfaz conversacional alrededor de un modelo y reglas. |
| Workflow | Secuencia de pasos definida por el desarrollador. |
| Agente | Puede seleccionar acciones, herramientas y siguientes pasos dentro de un objetivo y restricciones. |
| Sistema multiagente | Varios agentes especializados coordinan tareas o roles. |

La frontera no siempre es absoluta: un sistema puede combinar workflows deterministas con decisiones agentivas.

## 3. Evolución conceptual

1. Modelos estadísticos y ML.
2. Deep learning.
3. LLM y modelos multimodales.
4. RAG.
5. Tool/function calling.
6. Workflows LLM.
7. Agentes con bucles de decisión y ejecución.
8. Multiagente.
9. Sistemas interoperables con memoria, evaluación, observabilidad y control de permisos.

## 4. Arquitectura de referencia

### 4.1 Componentes

**Modelo:** produce decisiones, planes, argumentos de herramientas y respuestas.

**Objetivo e instrucciones:** definen qué se intenta conseguir y qué límites deben respetarse.

**Estado/contexto:** contiene información de la ejecución actual, historial relevante, resultados de herramientas y variables de control.

**Memoria:** conserva información entre ejecuciones cuando el diseño lo requiere.

**Herramientas:** APIs, bases de datos, buscadores, navegadores, sistemas de archivos, código, sensores o aplicaciones.

**Orquestador/runtime:** controla el ciclo, errores, timeouts, handoffs, reintentos y terminación.

**Evaluación/observabilidad:** registra trazas, resultados, costos, latencia, errores y éxito de tareas.

**Guardrails y permisos:** restringen qué puede hacer el agente y cuándo requiere aprobación humana.

### 4.2 Bucle agentivo

OBJETIVO → OBSERVAR → INTERPRETAR → PLANEAR → VALIDAR PERMISOS → EJECUTAR HERRAMIENTA → OBSERVAR RESULTADO → EVALUAR → RESPONDER o REPETIR.

## 5. Herramientas y function calling

Una herramienta debe exponer un contrato claro: nombre, descripción, parámetros, tipos, permisos y resultado esperado. El agente puede generar una llamada estructurada y el runtime decide si se ejecuta.

Buenas prácticas: validación de esquemas; mínimo privilegio; timeouts; límites de llamadas; sanitización de entradas; confirmación humana para acciones de alto impacto; registro de cada invocación; aislamiento de credenciales.

MCP y otros protocolos buscan estandarizar la conexión entre modelos/agentes y herramientas o fuentes de contexto. La interoperabilidad no elimina la necesidad de autorización.

## 6. Memoria

**Corto plazo:** información de la ejecución actual.

**Persistente:** datos entre sesiones.

**Semántica:** hechos, conceptos y relaciones recuperables.

**Episódica:** registro de experiencias o ejecuciones anteriores.

**Procedimental:** reglas o procedimientos sobre cómo ejecutar tareas.

Una memoria agentiva debe controlar retención, actualización, relevancia, privacidad y procedencia.

## 7. RAG y conocimiento

RAG separa la generación del conocimiento almacenado. Flujo típico: consulta → recuperación → filtrado/ranking → contexto → generación → verificación.

RAG puede convertirse en una herramienta del agente. Un sistema RAG puede limitarse a recuperar documentos, mientras un agente puede decidir cuándo buscar, qué fuente usar, combinar resultados y ejecutar acciones posteriores.

## 8. Planificación y razonamiento

Patrones frecuentes: ReAct; Plan-and-Execute; Reflection; planificación jerárquica; delegación multiagente.

Ningún patrón garantiza corrección. La calidad depende del modelo, herramientas, estado, datos, validadores y evaluación.

## 9. Multiagente

Arquitecturas frecuentes: supervisor + especialistas; agentes en cadena; revisión; paralelización; handoffs; jerarquías.

Ventajas potenciales: separación de responsabilidades, especialización y paralelización. Costos: mayor complejidad, latencia, tokens, coordinación, superficie de ataque y dificultad de depuración. Más agentes no equivale automáticamente a mejor sistema.

## 10. Autonomía

Una taxonomía práctica: 0 generación sin herramientas; 1 herramientas con flujo predeterminado; 2 selección de herramientas; 3 planificación multipaso; 4 ejecución prolongada con memoria; 5 coordinación multiagente. No es un estándar universal.

## 11. Evaluación

Medir: tasa de éxito; exactitud; éxito de herramientas; recuperación ante errores; latencia; costo; número de pasos; tokens; groundedness/procedencia; violaciones de políticas; acciones no autorizadas; estabilidad ante entradas adversariales.

La evaluación debe incluir casos normales, ambiguos y adversariales.

## 12. Seguridad

OWASP publicó el Top 10 for Agentic Applications 2026. La capacidad de actuar introduce riesgos adicionales respecto de un chatbot.

Amenazas: prompt injection; tool poisoning; abuso de herramientas; escalamiento de privilegios; exfiltración; credenciales expuestas; acciones excesivas; memoria contaminada; dependencias externas; fallas de supervisión y trazabilidad.

Controles: mínimo privilegio; separación de credenciales; allowlists; validación de argumentos; sandboxing; human-in-the-loop; límites de tiempo/presupuesto; observabilidad; pruebas adversariales; rollback o recuperación.

## 13. Interoperabilidad

Conceptos: MCP para conexión entre clientes/agentes y herramientas o recursos; A2A para comunicación entre agentes; APIs; webhooks; colas; function/tool calling.

NIST señaló en 2026 la interoperabilidad como objetivo de su iniciativa de estándares para agentes.

## 14. Ecosistema de frameworks

### OpenAI Agents SDK
SDK code-first para Python y TypeScript. Integra agentes, herramientas, handoffs, guardrails, estado y observabilidad. El SDK es software de desarrollo; el costo de inferencia depende del proveedor/modelo.

### Microsoft Agent Framework
SDK open source para agentes, workflows, memoria/persistencia, herramientas, RAG, middleware, seguridad y orquestación. Documenta soporte para Python y .NET.

### Google Agent Development Kit (ADK)
Framework de Google para construir agentes y sistemas multiagente con herramientas y opciones de despliegue.

### LangGraph
Framework de orquestación de bajo nivel para agentes stateful y de larga duración, con control de estado, ciclos, interrupciones y ejecución.

### CrewAI
Framework orientado a equipos de agentes y flujos de trabajo, con separación de roles y tareas.

### AutoGen
Framework multiagente de Microsoft. En 2026 está en maintenance mode; Microsoft dirige a nuevos usuarios hacia Agent Framework.

### LlamaIndex
Framework para aplicaciones con datos, recuperación, agentes y workflows.

### Haystack
Framework open source para pipelines, RAG, herramientas y agentes.

### Semantic Kernel
SDK open source de Microsoft para integrar modelos con plugins, memoria, procesos y agentes.

### Dify
Plataforma open source visual para aplicaciones LLM, workflows, agentes, herramientas y RAG; puede autoalojarse.

### Flowise
Constructor visual para aplicaciones LLM y agentes, útil para prototipos y flujos visuales.

### OpenHands
Plataforma open source centrada en agentes de desarrollo de software que interactúan con herramientas y entornos de programación.

### Browser Use
Framework open source para agentes que interactúan con navegadores. Puede ejecutarse localmente con modelos compatibles; los modelos/servicios conectados pueden tener costo.

## 15. Gratis vs open source

| Modalidad | Significado |
|---|---|
| Open source | Código disponible bajo una licencia determinada. |
| Self-hosted | Puede ejecutarse en infraestructura propia. |
| Free tier | Servicio comercial con cuota gratuita limitada. |
| Modelo local | Inferencia en hardware propio. |
| API gratuita | Uso sin pago hasta un límite del proveedor. |

Una solución de bajo costo puede combinar framework open source + modelo local + herramientas locales.

## 16. Arquitecturas de despliegue

**Local:** privacidad y control; limitaciones de RAM, GPU, latencia y capacidad.

**Cloud:** escalabilidad; limitaciones de costo, dependencia y tratamiento de datos.

**Híbrida:** modelo local para tareas económicas y servicios externos para tareas difíciles.

## 17. Cómo elegir

Criterios: licencia; lenguaje; ejecución local; proveedores; herramientas; memoria; multiagente; RAG; observabilidad; seguridad; comunidad/adopción; estabilidad; documentación; costo total; facilidad de migración.

No existe una única opción adecuada para todos los proyectos.

## 18. Arquitectura mínima para aprender

Usuario → Agente → Modelo + Estado + Herramientas + Memoria + Validador + Registro de ejecución.

Comenzar con un agente y pocas herramientas permite observar el ciclo completo antes de introducir multiagente.

## 19. Ejemplo

Objetivo: analizar un CSV y encontrar anomalías.

1. Recibir objetivo.
2. Inspeccionar archivo.
3. Elegir herramienta.
4. Ejecutar análisis.
5. Observar estadísticas.
6. Calcular métricas adicionales.
7. Evaluar anomalías.
8. Generar informe.
9. Guardar resultado.
10. Responder con evidencia y trazabilidad.

El modelo no es todo el sistema: herramientas, estado, validaciones y ejecución son esenciales.

## 20. Relación con software tradicional

Una arquitectura robusta suele combinar: modelo para interpretación y decisiones flexibles; código para validación y cálculo exacto; base de datos para persistencia; herramientas para acciones; políticas para límites; evaluación para comprobación.

## 21. Tendencias 2026

Runtimes con memoria persistente; interoperabilidad; agentes de larga duración; evaluación automática; trazas; human-in-the-loop; agentes de software; browser agents; modelos locales; seguridad agentiva; arquitecturas híbridas workflow + agent; estandarización de herramientas y comunicación agente-agente.

## 22. Conclusiones

La IA agentiva debe entenderse como una arquitectura de sistemas, no solamente como un modelo de lenguaje. La capacidad de observar, decidir, utilizar herramientas, conservar estado y actuar convierte la seguridad, evaluación y gobernanza en componentes técnicos centrales.

Para proyectos de bajo costo, frameworks open source y modelos locales permiten experimentar sin depender exclusivamente de APIs comerciales. Sin embargo, open source no implica que todos los modelos, servicios, datos o herramientas sean gratuitos.

## 23. Fuentes oficiales

NIST: https://www.nist.gov/news-events/news/2026/02/announcing-ai-agent-standards-initiative-interoperable-and-secure
OpenAI Agents SDK: https://developers.openai.com/api/docs/guides/agents/sdk
Microsoft Agent Framework: https://learn.microsoft.com/en-us/agent-framework
Anthropic: https://www.anthropic.com/research/building-effective-agents
OWASP: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
LangGraph: https://github.com/langchain-ai/langgraph
CrewAI: https://github.com/crewAIInc/crewAI
AutoGen: https://github.com/microsoft/autogen
Google ADK: https://github.com/google/adk-python
LlamaIndex: https://github.com/run-llama/llama_index
Haystack: https://github.com/deepset-ai/haystack
Semantic Kernel: https://github.com/microsoft/semantic-kernel
Dify: https://github.com/langgenius/dify
Flowise: https://github.com/FlowiseAI/Flowise
OpenHands: https://github.com/All-Hands-AI/OpenHands
Browser Use: https://github.com/browser-use/browser-use

Nota metodológica: “más usadas” se trata mediante señales de adopción pública como actividad, estrellas, documentación, comunidad y disponibilidad; esas señales no equivalen a una medición universal de usuarios activos.
