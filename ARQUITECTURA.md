# Desktop Voice-to-Text App - Arquitectura

## Descripción General

Aplicación de escritorio que permite convertir voz a texto mediante un hotkey global, insertando el texto transcrito directamente en cualquier campo de entrada activo.

## Stack Tecnológico

### Desktop App
- **Electron**: Framework para aplicación de escritorio multiplataforma
- **TypeScript**: Lenguaje principal
- **Node.js**: Runtime para procesos del sistema

### Backend (Opcional)
- **FastAPI**: API minimalista para procesamiento
- **OpenAI Whisper**: Servicio de transcripción de voz

## Arquitectura de la Aplicación

### Procesos de Electron

1. **Main Process**
   - Gestión de ventanas
   - Registro de hotkeys globales
   - Comunicación con el sistema operativo
   - Gestión del system tray

2. **Renderer Process**
   - Ventana de visualización de audio
   - Ventana de configuración
   - UI mínima con controles

3. **Preload Script**
   - Bridge seguro entre main y renderer
   - APIs expuestas para audio y sistema

## Flujo Principal

```
1. Usuario presiona hotkey (ej: Ctrl+Shift+V)
   ↓
2. App detecta el hotkey y activa captura de audio
   ↓
3. Muestra visualizador de audio flotante
   ↓
4. Captura audio del micrófono
   ↓
5. Usuario suelta hotkey o detecta silencio
   ↓
6. Envía audio a Whisper API
   ↓
7. Recibe transcripción
   ↓
8. Inserta texto en campo activo
   ↓
9. Oculta visualizador
```

## Módulos Principales

### 1. Audio Capture Module
```typescript
interface AudioCapture {
  startRecording(): void
  stopRecording(): Buffer
  getAudioLevel(): number
}
```

### 2. Hotkey Manager
```typescript
interface HotkeyManager {
  register(combination: string, callback: Function): void
  unregister(combination: string): void
  isPressed(): boolean
}
```

### 3. System Integration
```typescript
interface SystemIntegration {
  insertText(text: string): void
  getActiveWindow(): WindowInfo
  isFocusedOnTextInput(): boolean
}
```

### 4. Transcription Service
```typescript
interface TranscriptionService {
  transcribe(audio: Buffer): Promise<string>
  setLanguage(lang: string): void
}
```

## Estructura de Directorios

```
voice-to-text-desktop/
├── desktop-app/
│   ├── src/
│   │   ├── main/
│   │   │   ├── index.ts
│   │   │   ├── hotkey.ts
│   │   │   ├── tray.ts
│   │   │   └── ipc-handlers.ts
│   │   ├── renderer/
│   │   │   ├── visualizer/
│   │   │   └── settings/
│   │   ├── preload/
│   │   │   └── index.ts
│   │   └── shared/
│   │       └── types.ts
│   ├── assets/
│   │   └── icons/
│   ├── package.json
│   └── electron-builder.yml
├── backend/ (opcional)
│   ├── main.py
│   ├── transcription.py
│   └── requirements.txt
└── README.md
```

## Configuración Mínima

### Variables de Entorno
```
OPENAI_API_KEY=tu_api_key
DEFAULT_LANGUAGE=es
DEFAULT_HOTKEY=CommandOrControl+Shift+V
```

### Configuración de Usuario (JSON)
```json
{
  "hotkey": "Ctrl+Shift+V",
  "language": "es",
  "microphone": "default",
  "mode": "push-to-talk",
  "sensitivity": 0.5
}
```

## Consideraciones Técnicas

### Rendimiento
- Proceso de audio en thread separado
- Lazy loading de módulos pesados
- Liberación de recursos cuando está inactivo

### Seguridad
- Sandboxing de Electron activado
- Validación de entrada de audio
- Rate limiting para API calls

### Compatibilidad
- Windows 10+
- macOS 10.15+
- Linux (Ubuntu 20.04+)

## Dependencias Principales

### Desktop App
```json
{
  "electron": "^27.0.0",
  "node-record-lpcm16": "^1.0.1",
  "robotjs": "^0.6.0",
  "axios": "^1.6.0"
}
```

### Backend (si se usa)
```python
fastapi==0.104.1
openai==1.3.0
python-multipart==0.0.6
```

## Decisiones de Diseño

1. **Electron vs Alternativas**: Elegido por compatibilidad multiplataforma y ecosistema maduro
2. **Hotkey Global**: Necesario para activación desde cualquier aplicación
3. **Visualización Flotante**: Feedback inmediato al usuario sin interrumpir flujo
4. **Whisper API**: Mejor precisión que alternativas open source
5. **Arquitectura Simple**: Sin base de datos, sin autenticación, sin persistencia