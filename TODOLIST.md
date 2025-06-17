# Desktop Voice-to-Text App - Lista de Tareas

## 1. Configuración Inicial

### 1.1 Setup del Proyecto
- [ ] Crear estructura de carpetas (desktop-app/, backend/)
- [ ] Crear README.md del proyecto

### 1.2 Configuración Desktop App (Electron)
- [ ] Inicializar proyecto Electron con TypeScript
- [ ] Configurar estructura básica (main, renderer, preload)
- [ ] Instalar dependencias para audio (node-record-lpcm16 o similar)
- [ ] Configurar empaquetado para Windows/Mac/Linux

### 1.3 Configuración Backend (FastAPI)
- [ ] Crear proyecto FastAPI mínimo
- [ ] Configurar cliente de OpenAI para Whisper
- [ ] Crear endpoint único para transcripción

## 2. Sistema de Captura de Voz

### 2.1 Hotkey Global
- [ ] Implementar registro de hotkey global (ej: Ctrl+Shift+V)
- [ ] Detectar cuando se presiona/suelta la tecla
- [ ] Sistema para cambiar hotkey desde configuración

### 2.2 Captura de Audio
- [ ] Implementar captura de audio del micrófono
- [ ] Detección de actividad de voz (VAD)
- [ ] Conversión de audio a formato compatible con Whisper
- [ ] Sistema de buffer para audio en streaming

### 2.3 Visualización de Audio
- [ ] Crear ventana flotante transparente
- [ ] Implementar visualizador de forma de onda en tiempo real
- [ ] Indicador visual de estado (escuchando/procesando)
- [ ] Auto-ocultar cuando no está en uso

## 3. Integración con Sistema

### 3.1 Detección de Input Activo
- [ ] Detectar aplicación y campo de texto activo
- [ ] Obtener posición del cursor
- [ ] Verificar que el campo acepta entrada de texto

### 3.2 Inserción de Texto
- [ ] Implementar inyección de texto en campo activo
- [ ] Manejo de diferentes tipos de campos (web, nativo, terminal)
- [ ] Preservar formato y posición del cursor

## 4. Procesamiento de Voz

### 4.1 Cliente de Transcripción
- [ ] Enviar audio a Whisper API
- [ ] Manejo de errores y reintentos
- [ ] Optimización de latencia

### 4.2 Post-procesamiento
- [ ] Corrección básica de puntuación
- [ ] Detección de comandos especiales (nueva línea, borrar, etc.)
- [ ] Capitalización inteligente

## 5. Interfaz Mínima

### 5.1 Bandeja del Sistema
- [ ] Icono en system tray
- [ ] Menú contextual (configuración, salir)
- [ ] Indicador de estado (activo/inactivo)

### 5.2 Ventana de Configuración
- [ ] Selección de micrófono
- [ ] Configuración de hotkey
- [ ] Ajuste de sensibilidad de voz
- [ ] Idioma de transcripción

## 6. Funcionalidades Core

### 6.1 Modos de Captura
- [ ] Modo push-to-talk (mantener presionado)
- [ ] Modo toggle (presionar para iniciar/detener)
- [ ] Detección automática de silencio

### 6.2 Rendimiento
- [ ] Minimizar uso de CPU cuando está inactivo
- [ ] Inicio rápido de captura (< 100ms)
- [ ] Liberación de recursos cuando no se usa

## 7. Testing y Empaquetado

### 7.1 Testing
- [ ] Test de captura de audio
- [ ] Test de hotkeys en diferentes aplicaciones
- [ ] Test de inserción de texto

### 7.2 Distribución
- [ ] Crear instalador para Windows
- [ ] Crear DMG para macOS
- [ ] Crear AppImage para Linux
- [ ] Firma de código para evitar warnings de seguridad

## 8. MVP Final

### 8.1 Estabilidad
- [ ] Manejo robusto de errores
- [ ] Logs para debugging
- [ ] Recuperación automática de fallos

### 8.2 Documentación Mínima
- [ ] Instrucciones de instalación
- [ ] Guía de uso básico
- [ ] Requisitos del sistema