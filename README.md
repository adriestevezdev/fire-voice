# Fire Voice - Desktop Voice-to-Text Application

A desktop application that converts voice to text using OpenAI's Whisper API. Built with Electron for the desktop client and FastAPI for the backend.

## Project Structure

```
fire-voice/
├── desktop-app/        # Electron desktop application
│   ├── src/           # TypeScript source files
│   ├── dist/          # Compiled JavaScript files
│   └── package.json   # Node.js dependencies
├── backend/           # FastAPI backend server
│   ├── app/           # Python application code
│   ├── main.py        # Application entry point
│   └── requirements.txt # Python dependencies
└── TODOLIST.md        # Development roadmap
```

## Prerequisites

- Node.js 16+ and npm
- Python 3.8+
- OpenAI API key

## Setup

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file based on `.env.example`:
   ```bash
   cp .env.example .env
   ```

5. Add your OpenAI API key to the `.env` file:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

6. Run the backend server:
   ```bash
   python main.py
   ```

   The API will be available at `http://localhost:8000`

### Desktop App Setup

1. Navigate to the desktop-app directory:
   ```bash
   cd desktop-app
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Build and run the application:
   ```bash
   npm start
   ```

## API Endpoints

- `GET /` - API information
- `GET /api/health` - Health check
- `POST /api/transcribe` - Transcribe audio file
- `WebSocket /ws/transcribe` - Real-time audio transcription

## Development

### Backend Development

Run the backend in development mode with auto-reload:
```bash
cd backend
source venv/bin/activate
python main.py
```

### Desktop App Development

Run TypeScript compiler in watch mode:
```bash
cd desktop-app
npm run dev
```

In another terminal, run Electron:
```bash
cd desktop-app
electron .
```

## Features (In Development)

- [x] Basic project structure
- [x] Electron desktop app with TypeScript
- [x] FastAPI backend with Whisper integration
- [ ] Global hotkey for voice capture
- [ ] Real-time audio visualization
- [ ] System tray integration
- [ ] Cross-platform support (Windows, macOS, Linux)

## License

This project is licensed under the MIT License.