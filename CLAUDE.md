# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Fire Voice is a desktop voice-to-text application built with Electron and FastAPI. It captures audio via global hotkeys and transcribes it using OpenAI's Whisper API, then inserts the text into the active input field.

## Architecture

The project consists of two main components:

### Desktop App (Electron + TypeScript)
- **Main Process**: Handles window management, global hotkeys, system tray integration
- **Renderer Process**: Audio visualization UI and settings windows  
- **Preload Script**: Secure bridge between main and renderer processes
- **Audio Capture**: Uses `node-record-lpcm16` for microphone recording

### Backend (FastAPI + Python)
- **REST API**: `/api/transcribe` endpoint for audio file transcription
- **WebSocket**: `/ws/transcribe` for real-time audio streaming
- **OpenAI Integration**: Uses Whisper API for speech-to-text conversion

## Development Commands

### Desktop App
```bash
cd desktop-app
npm install                    # Install dependencies
npm run build                  # Compile TypeScript to JavaScript
npm start                      # Build and run Electron app
npm run dev                    # Run TypeScript compiler in watch mode
```

### Backend
```bash
cd backend
python3 -m venv venv          # Create virtual environment
source venv/bin/activate      # Activate venv (Linux/Mac)
pip install -r requirements.txt  # Install Python dependencies
python main.py                # Run FastAPI server on localhost:8000
```

### Building & Packaging
```bash
cd desktop-app
npm run pack                  # Create unpacked build
npm run dist                  # Create distributable packages
npm run dist:win              # Build for Windows (NSIS installer)
npm run dist:mac              # Build for macOS (DMG)
npm run dist:linux            # Build for Linux (AppImage)
```

## Configuration

### Environment Variables
Backend requires `.env` file in the `backend/` directory:
```
OPENAI_API_KEY=your_openai_api_key_here
DEBUG=false
HOST=127.0.0.1
PORT=8000
```

### Build Configuration
Electron Builder config is in `desktop-app/package.json` under the `"build"` section. Icons should be placed in `desktop-app/assets/` directory.

## Key Technical Details

### Audio Flow
1. Global hotkey triggers audio recording
2. Audio buffer captured using `node-record-lpcm16`
3. Audio sent to backend `/api/transcribe` or `/ws/transcribe`
4. Whisper API returns transcription
5. Text inserted into active system input field

### Process Communication
- Main ↔ Renderer: IPC (contextIsolation enabled for security)
- Desktop ↔ Backend: HTTP/WebSocket API calls
- System Integration: Planned for text insertion and window detection

### Cross-Platform Support
- Windows: NSIS installer
- macOS: DMG package  
- Linux: AppImage format

## File Structure
```
desktop-app/src/
├── main.ts          # Main Electron process
├── renderer.ts      # Renderer process UI logic  
├── preload.ts       # IPC bridge script
└── index.html       # Main window HTML

backend/app/
├── main.py          # FastAPI application
├── config.py        # Settings and environment variables
└── services/openai_service.py  # Whisper API integration
```

## Development Status
This is an early-stage project. Core transcription functionality is implemented, but global hotkeys, audio visualization, and system text insertion are still in development. See `TODOLIST.md` for detailed progress tracking.