from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Proyecto DevOps</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --primary: #3498db;
            --secondary: #2c3e50;
            --accent: #e74c3c;
            --light: #ecf0f1;
            --dark: #2c3e50;
            --success: #2ecc71;
            --gradient: linear-gradient(135deg, #3498db, #2c3e50);
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        body {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            color: var(--dark);
            line-height: 1.6;
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            max-width: 1000px;
            margin: 0 auto;
        }
        
        .header {
            background: var(--gradient);
            color: white;
            padding: 40px 30px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
            margin-bottom: 30px;
            position: relative;
            overflow: hidden;
        }
        
        .header::before {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" preserveAspectRatio="none"><path d="M0,0 L100,0 L100,100 Z" fill="rgba(255,255,255,0.1)"/></svg>');
            background-size: cover;
        }
        
        .header h1 {
            font-size: 2.5rem;
            margin-bottom: 15px;
            position: relative;
        }
        
        .header h2 {
            font-size: 1.5rem;
            font-weight: 400;
            margin-bottom: 10px;
            position: relative;
        }
        
        .header h3 {
            font-size: 1.2rem;
            font-weight: 400;
            margin-bottom: 5px;
            position: relative;
        }
        
        .content {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 25px;
            margin-bottom: 30px;
        }
        
        .card {
            background: white;
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);
        }
        
        .card h3 {
            color: var(--primary);
            margin-bottom: 15px;
            font-size: 1.4rem;
            display: flex;
            align-items: center;
        }
        
        .card h3 i {
            margin-right: 10px;
            color: var(--accent);
        }
        
        .status {
            background: var(--success);
            color: white;
            padding: 15px 25px;
            border-radius: 50px;
            text-align: center;
            font-size: 1.2rem;
            font-weight: 600;
            box-shadow: 0 5px 15px rgba(46, 204, 113, 0.4);
            margin-bottom: 30px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .status i {
            margin-right: 10px;
            font-size: 1.5rem;
        }
        
        .tech-icons {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 20px;
            margin-top: 30px;
        }
        
        .tech-icon {
            background: white;
            width: 70px;
            height: 70px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            font-size: 2rem;
            color: var(--primary);
            transition: transform 0.3s ease;
        }
        
        .tech-icon:hover {
            transform: scale(1.1);
        }
        
        .footer {
            text-align: center;
            margin-top: 40px;
            padding: 20px;
            color: var(--dark);
            font-size: 0.9rem;
            opacity: 0.8;
        }
        
        @media (max-width: 768px) {
            .header h1 {
                font-size: 2rem;
            }
            
            .header h2 {
                font-size: 1.3rem;
            }
            
            .content {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1><i class="fas fa-code-branch"></i> Proyecto Final - Automatización DevOps</h1>
            <h2>Materia: Automatizacion de infraestructura digital II/h2>
            <h3><i class="fas fa-user-tie"></i> Profesor: Froylan Alonso Perez Alanis</h3>
            <h3><i class="fas fa-user-graduate"></i> Alumno: Grau Moreno Manuel - 220550</h3>
        </div>
        
        <div class="status">
            <i class="fas fa-check-circle"></i> Aplicación ejecutándose correctamente
        </div>
        
        <div class="content">
            <div class="card">
                <h3><i class="fas fa-tasks"></i> Objetivos del Proyecto</h3>
                <p>Implementar un pipeline de CI/CD completo que automatice el proceso de desarrollo, pruebas y despliegue de aplicaciones.</p>
            </div>
            
            <div class="card">
                <h3><i class="fas fa-cogs"></i> Tecnologías Utilizadas</h3>
                <p>Git, Jenkins, Docker, Kubernetes, Ansible, Terraform, AWS, entre otras herramientas del ecosistema DevOps.</p>
            </div>
            
            <div class="card">
                <h3><i class="fas fa-rocket"></i> Metodología</h3>
                <p>Implementación de prácticas ágiles con integración y entrega continua para garantizar calidad y rapidez en el desarrollo.</p>
            </div>
        </div>
        
        <div class="tech-icons">
            <div class="tech-icon"><i class="fab fa-git-alt"></i></div>
            <div class="tech-icon"><i class="fab fa-jenkins"></i></div>
            <div class="tech-icon"><i class="fab fa-docker"></i></div>
            <div class="tech-icon"><i class="fab fa-aws"></i></div>
            <div class="tech-icon"><i class="fab fa-linux"></i></div>
        </div>
        
        <div class="footer">
            <p>Proyecto Final - Herramientas de Automatización en DevOps | 01/OCT/2025</p>
        </div>
    </div>
</body>
</html>
    '''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)