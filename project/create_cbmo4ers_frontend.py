#!/usr/bin/env python3
import os, textwrap

BASE = os.path.join(os.getcwd(), "frontend")

FILES = {
  "frontend": {
    "README.md": textwrap.dedent("""\
      # CBMo4ers Frontend

      ## Setup

      ```bash
      npm install
      npm run dev
      ```

      ## Build

      ```bash
      npm run build
      ```

      ## Environment

      Copy `.env.example` to `.env` and set `VITE_API_URL` to your backend URL.
      """),

    "package.json": textwrap.dedent("""\
      {
        "name": "cbmo4ers-frontend",
        "version": "1.0.0",
        "scripts": {
          "dev": "vite",
          "build": "vite build",
          "preview": "vite preview"
        },
        "dependencies": {
          "react": "^18.2.0",
          "react-dom": "^18.2.0",
          "antd": "^5.9.1"
        },
        "devDependencies": {
          "vite": "^5.4.19",
          "@vitejs/plugin-react": "^4.5.2",
          "tailwindcss": "^3.3.2",
          "postcss": "^8.4.21",
          "autoprefixer": "^10.4.14"
        }
      }
      """),

    ".env.example": textwrap.dedent("""\
      VITE_API_URL=http://localhost:5002
      """),

    "postcss.config.js": textwrap.dedent("""\
      module.exports = {
        plugins: {
          tailwindcss: {},
          autoprefixer: {},
        },
      };
      """),

    "tailwind.config.js": textwrap.dedent("""\
      module.exports = {
        darkMode: 'class',
        content: ['./src/**/*.{js,jsx,ts,tsx}'],
        theme: {
          extend: {
            colors: {
              bhabit: {
                black: '#000000',
                purple: '#7D00FF',
                orange: '#FF5E00',
                blue: '#00CFFF',
                offwhite: '#E0E0E0',
                gray: '#6E6E6E',
                error: '#FF3B30',
              },
            },
            fontFamily: {
              primary: ['Space Grotesk', 'sans-serif'],
              secondary: ['Inter', 'sans-serif'],
            },
          },
        },
        plugins: [],
      };
      """),

    "vite.config.js": textwrap.dedent("""\
      import { defineConfig } from 'vite';
      import react from '@vitejs/plugin-react';

      export default defineConfig({
        plugins: [react()],
        define: { 'process.env': process.env },
      });
      """),

    "public/index.html": textwrap.dedent("""\
      <!DOCTYPE html>
      <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>CBMo4ers</title>
      </head>
      <body class="bg-black">
        <div id="root"></div>
        <script type="module" src="/src/main.jsx"></script>
      </body>
      </html>
      """),

    "src/index.css": textwrap.dedent("""\
      @tailwind base;
      @tailwind components;
      @tailwind utilities;
      """),

    "src/main.jsx": textwrap.dedent("""\
      import React from 'react';
      import ReactDOM from 'react-dom/client';
      import App from './App.jsx';
      import './index.css';

      ReactDOM.createRoot(document.getElementById('root')).render(
        <React.StrictMode>
          <App />
        </React.StrictMode>
      );
      """),

    "src/App.jsx": textwrap.dedent("""\
      import React from 'react';
      import SplashScreen from './components/SplashScreen.jsx';
      import TopBannerScroll from './components/TopBannerScroll.jsx';
      import GainersTable from './components/GainersTable.jsx';
      import LosersTable from './components/LosersTable.jsx';
      import VolumeBannerScroll from './components/VolumeBannerScroll.jsx';

      export default function App() {
        return (
          <div className="bg-black text-[#E0E0E0] min-h-screen">
            <SplashScreen />
            <div className="p-4">
              <TopBannerScroll />
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4 my-8">
                <GainersTable />
                <LosersTable />
              </div>
              <VolumeBannerScroll />
            </div>
          </div>
        );
      }
      """),

    "src/components/SplashScreen.jsx": textwrap.dedent("""\
      import React from 'react';
      export default function SplashScreen() {
        return (
          <div className="w-full h-48 flex items-center justify-center">
            <h1 className="text-4xl font-bold text-[#FF5E00]">BHABIT</h1>
          </div>
        );
      }
      """),

    "src/components/TopBannerScroll.jsx": textwrap.dedent("""\
      import React from 'react';
      export default function TopBannerScroll() {
        return (
          <div className="h-16 bg-gray-900 text-white flex items-center px-4">
            Top Banner Scroll Placeholder
          </div>
        );
      }
      """),

    "src/components/VolumeBannerScroll.jsx": textwrap.dedent("""\
      import React from 'react';
      export default function VolumeBannerScroll() {
        return (
          <div className="h-16 bg-gray-900 text-white flex items-center px-4">
            Volume Banner Scroll Placeholder
          </div>
        );
      }
      """),

    "src/components/GainersTable.jsx": textwrap.dedent("""\
      import React from 'react';
      export default function GainersTable() {
        return (
          <div className="bg-gray-800 p-4 rounded">
            Gainers Table Placeholder
          </div>
        );
      }
      """),

    "src/components/LosersTable.jsx": textwrap.dedent("""\
      import React from 'react';
      export default function LosersTable() {
        return (
          <div className="bg-gray-800 p-4 rounded">
            Losers Table Placeholder
          </div>
        );
      }
      """),
  }
}

def write_tree(base, tree):
    for name, content in tree.items():
        path = os.path.join(base, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            write_tree(path, content)
        else:
            with open(path, 'w') as f:
                f.write(content)

if __name__ == '__main__':
    if os.path.exists('frontend'):
        print("Error: 'frontend/' already exists. Remove or rename it first.")
        exit(1)
    write_tree(os.getcwd(), FILES)
    print("✅ `frontend/` scaffolded successfully.")
