# SaveIt - AI-Powered Bookmark Manager

A modern bookmark manager that uses AI to automatically summarize, categorize, and organize your saved links with a smart folder structure.

## 🚀 Quick Start

### Prerequisites

- **Docker** and **Docker Compose**
- **Git**

### Installation & Setup

1. **Clone the repository:**
   ```
   git clone https://github.com/Wanderer0074348/SaveIt.git
   cd SaveIt
   ```

2. **Set up environment variables:**
   
   Create a `.env` file in the `backend/` directory:
   ```
   cd backend
   touch .env
   ```
   
   Add your MongoDB Atlas connection string to `.env`:
   ```
   MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/saveit_db?retryWrites=true&w=majority
   ```

3. **Start the application:**
   ```
   # From the SaveIt/ root directory
   docker-compose up --build
   ```

4. **Access the application:**
   - **Frontend:** [http://localhost:3000](http://localhost:3000)
   - **Backend API:** [http://localhost:8000](http://localhost:8000)
   - **API Documentation:** [http://localhost:8000/docs](http://localhost:8000/docs)

## 🛠️ Development

### Project Structure
```
SaveIt/
├── backend/           # Python FastAPI backend
│   ├── main.py
│   ├── database/      # MongoDB models and operations
│   ├── api/           # API routes
│   └── requirements.txt
├── frontend/          # React + Tailwind CSS frontend
│   ├── src/
│   ├── components/
│   └── package.json
└── docker-compose.yml
```

### Testing the API

**Add a link:**
```
curl -X POST http://localhost:8000/api/links/ \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.google.com", "title": "Google"}'
```

**Get all links:**
```
curl http://localhost:8000/api/links/
```

### Local Development (Optional)

**Backend:**
```
cd backend
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

**Frontend:**
```
cd frontend
npm install
npm run dev
```

## 🔧 Common Issues

### Docker Permission Errors
```
sudo usermod -aG docker $USER
newgrp docker
```

### Port Already in Use
- Stop other services using ports 3000 or 8000
- Or modify ports in `docker-compose.yml`

### MongoDB Connection Issues
- Verify your `MONGODB_URI` in the `.env` file
- Ensure your MongoDB Atlas cluster allows connections from your IP

## 📝 Features

- ✅ Add and save links
- ✅ Modern React + Tailwind CSS frontend
- ✅ FastAPI backend with MongoDB
- 🚧 AI summarization (coming soon)
- 🚧 Auto-categorization (coming soon)
- 🚧 Smart folder structure (coming soon)

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source. See the repository for license details.

**Need help?** Open an issue on GitHub or check the API documentation at [http://localhost:8000/docs](http://localhost:8000/docs) when running locally.
