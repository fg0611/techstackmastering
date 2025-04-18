### ☕ **Analogías SOLID aplicadas a una cafetería**  

1. **📌 SRP (Single Responsibility Principle - Principio de Responsabilidad Única):**  
   *"La máquina de café no debe también tostar pan."*  
   → Cada dispositivo tiene **una sola función** (hacer café ≠ tostar pan).  

2. **📌 OCP (Open/Closed Principle - Principio Abierto/Cerrado):**  
   *"Puedes añadir leche (extender) sin modificar la máquina."*  
   → La máquina permite **extensiones** (leche, jarabes) sin cambiar su código interno.  

3. **📌 LSP (Liskov Substitution Principle - Principio de Sustitución de Liskov):**  
   *"Un café descafeinado debe poder usarse como café normal."*  
   → Las variantes (**subtipo: descafeinado**) deben ser intercambiables con la clase base (**café**).  

4. **📌 ISP (Interface Segregation Principle - Principio de Segregación de Interfaces):**  
   *"No obligues a todos a usar azúcar si no lo desean."*  
   → Interfaces minimalistas: **azúcar** y **sin azúcar** son opciones separadas.  

5. **📌 DIP (Dependency Inversion Principle - Principio de Inversión de Dependencias):**  
   *"La taza depende de la interfaz 'LíquidoBebible', no de 'Café' directamente."*  
   → La taza acepta **cualquier líquido** (té, café, chocolate) que cumpla la interfaz.  
---
### 🎯 **Clave para recordar:**  
- **SOLID** son **reglas de diseño**, no leyes físicas, pero mejoran drásticamente tu código.  
- Estas analogías ayudan a entender **el "porqué"** detrás de cada principio.  