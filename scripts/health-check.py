import requests
import json
from datetime import datetime

def check_services():
    print("🔍 Verificando servicios...")
    
    try:
        # Verificar servicio web
        response = requests.get('http://localhost:5000', timeout=5)
        web_status = response.status_code == 200
        print(f"Servicio Web: {'ACTIVO' if web_status else 'INACTIVO'}")
    except:
        web_status = False
        print("Servicio Web: INACTIVO")
    
    try:
        # Verificar health endpoint
        response = requests.get('http://localhost:5000/health', timeout=5)
        health_status = response.status_code == 200
        print(f"Health Check: {'OK' if health_status else 'FAIL'}")
    except:
        health_status = False
        print("Health Check: FAIL")
    
    # Reporte final
    report = {
        "timestamp": datetime.now().isoformat(),
        "services": {
            "web_service": web_status,
            "health_endpoint": health_status
        },
        "overall": "HEALTHY" if (web_status and health_status) else "UNHEALTHY"
    }
    
    with open('health-report.json', 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\nEstado general: {report['overall']}")
    print("Reporte guardado en: health-report.json")

if __name__ == "__main__":
    check_services()