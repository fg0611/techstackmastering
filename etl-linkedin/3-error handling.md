¡Entendido! Vamos a hacer un "reset" completo para que puedas empezar de nuevo. Te guiaré paso a paso para eliminar todo lo relacionado con tu despliegue actual en AKS, limpiar las imágenes en Azure Container Registry (ACR) si es necesario, y luego volver a crear y subir tu imagen Docker.

---

## 1. **Eliminar los Pods y Recursos en AKS**

### a) Eliminar el Deployment

Primero, elimina el deployment para que se eliminen los pods asociados:

```bash
kubectl delete deployment job-api
```

Esto eliminará todos los pods que pertenecen al deployment `job-api`.

### b) Verificar que los Pods se Hayan Eliminado

Verifica que no haya pods en ejecución:

```bash
kubectl get pods
```

Si todo se eliminó correctamente, no deberías ver ningún pod relacionado con `job-api`.

### c) Eliminar el Servicio (si existe)

Si creaste un servicio para exponer tu API, elimínalo también:

```bash
kubectl delete service job-api-service
```

Reemplaza `job-api-service` con el nombre de tu servicio si es diferente.

---

## 2. **Eliminar Imágenes en Azure Container Registry (ACR)**

Si quieres eliminar las imágenes Docker que subiste a tu ACR, puedes hacerlo desde la CLI de Azure.

### a) Listar las Imágenes en el ACR

Primero, lista las imágenes en tu ACR:

```bash
az acr repository list --name mycontainerregistrykode --output table
```

Esto te mostrará una lista de repositorios (por ejemplo, `job-api`).

### b) Listar las Etiquetas de una Imagen

Si quieres ver las etiquetas de una imagen específica (por ejemplo, `job-api`):

```bash
az acr repository show-tags --name mycontainerregistrykode --repository job-api --output table
```

### c) Eliminar una Imagen

Para eliminar una imagen específica, usa el siguiente comando:

```bash
az acr repository delete --name mycontainerregistrykode --image job-api:latest --yes
```

Esto eliminará la imagen con la etiqueta `latest` del repositorio `job-api`.

Si quieres eliminar todas las imágenes de un repositorio, puedes usar:

```bash
az acr repository delete --name mycontainerregistrykode --repository job-api --yes
```

---

## 3. **Reconstruir y Subir la Imagen Docker**

Ahora que has limpiado todo, puedes reconstruir y subir tu imagen Docker.

### a) Reconstruir la Imagen Localmente

Navega al directorio donde está tu `Dockerfile` y reconstruye la imagen:

```bash
docker build -t job-api:latest .
```

### b) Etiquetar la Imagen para ACR

Etiqueta la imagen con la URL de tu ACR:

```bash
docker tag job-api:latest mycontainerregistrykode.azurecr.io/job-api:latest
```

### c) Iniciar Sesión en el ACR

Inicia sesión en tu ACR:

```bash
az acr login --name mycontainerregistrykode
```

### d) Subir la Imagen al ACR

Sube la imagen al ACR:

```bash
docker push mycontainerregistrykode.azurecr.io/job-api:latest
```

---

## 4. **Volver a Desplegar en AKS**

Ahora que la imagen está en el ACR, puedes volver a desplegar tu aplicación en AKS.

### a) Crear el Secret de Docker Registry (si no lo has hecho)

Si no has creado el secret para autenticarte con el ACR, hazlo ahora:

```bash
kubectl create secret docker-registry acr-credentials \
    --docker-server=mycontainerregistrykode.azurecr.io \
    --docker-username=<ACR_USERNAME> \
    --docker-password=<ACR_PASSWORD> \
    --docker-email=<TU_EMAIL>
```

Reemplaza `<ACR_USERNAME>`, `<ACR_PASSWORD>` y `<TU_EMAIL>` con las credenciales de tu ACR.

### b) Aplicar el Deployment

Aplica tu archivo `deployment.yaml`:

```bash
kubectl apply -f deployment.yaml
```

### c) Verificar el Estado del Deployment

Verifica que los pods se hayan creado correctamente:

```bash
kubectl get pods
```

Deberías ver los pods en estado `Running`.

---

## 5. **Conclusión**

Siguiendo estos pasos, habrás limpiado completamente tu entorno, eliminado las imágenes antiguas, reconstruido y subido una nueva imagen Docker, y desplegado tu aplicación en AKS. Si tienes más preguntas o necesitas ayuda adicional, ¡no dudes en preguntar! 🚀



kubectl logs <nombre-del-pod>




¡Entendido! Vamos a verificar por qué no estás obteniendo una respuesta al acceder a `http://134.33.145.128/jobs`. Hay varias cosas que podrían estar causando este problema. A continuación, te guiaré paso a paso para solucionarlo.

---

## 1. **Verificar el Endpoint Correcto**

Primero, asegúrate de que el endpoint `/jobs` esté correctamente definido en tu aplicación Flask. Por ejemplo, en tu código Flask, deberías tener algo como esto:

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/jobs', methods=['GET'])
def get_jobs():
    jobs = [{"id": 1, "title": "Developer"}, {"id": 2, "title": "Designer"}]
    return jsonify(jobs)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

Si tu endpoint está definido como `/jobs`, entonces la URL correcta sería:

```
http://134.33.145.128/jobs
```

---

## 2. **Verificar el Puerto del Servicio**

Tu servicio está configurado para escuchar en el puerto **80** (HTTP) y redirigir el tráfico al puerto **30688** en los pods. Sin embargo, tu aplicación Flask probablemente esté escuchando en el puerto **5000**.

### a) **Verificar el Puerto del Contenedor**

Revisa tu archivo `deployment.yaml` para asegurarte de que el puerto del contenedor esté correctamente configurado:

```yaml
spec:
  containers:
  - name: job-api
    image: mycontainerregistrykode.azurecr.io/job-api:latest
    ports:
    - containerPort: 5000  # Asegúrate de que sea el puerto correcto
```

### b) **Verificar el Puerto del Servicio**

Asegúrate de que el servicio esté redirigiendo el tráfico al puerto correcto del contenedor. Tu archivo `service.yaml` debería verse así:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: job-api-service
spec:
  type: LoadBalancer
  ports:
    - port: 80        # Puerto externo (HTTP)
      targetPort: 5000 # Puerto interno del contenedor
  selector:
    app: job-api
```

---

## 3. **Verificar los Logs del Pod**

Si el servicio y el puerto están correctamente configurados, pero aún no obtienes una respuesta, revisa los logs del pod para ver si hay errores.

### a) **Obtener el Nombre del Pod**

Ejecuta:

```bash
kubectl get pods
```

Deberías ver algo como esto:

```
NAME                       READY   STATUS    RESTARTS   AGE
job-api-576bffc59c-jp5p2   1/1     Running   0          5m
```

### b) **Verificar los Logs**

Revisa los logs del pod:

```bash
kubectl logs job-api-576bffc59c-jp5p2
```

Busca mensajes de error o advertencias que puedan indicar por qué la API no está respondiendo.

---

## 4. **Probar la API Dentro del Clúster**

Para asegurarte de que la API está funcionando correctamente, puedes probarla desde dentro del clúster.

### a) **Acceder al Pod**

Ejecuta un shell dentro del pod:

```bash
kubectl exec -it job-api-576bffc59c-jp5p2 -- /bin/sh
```

### b) **Probar la API con `curl`**

Dentro del pod, prueba la API con `curl`:

```bash
curl http://localhost:5000/jobs
```

Si obtienes una respuesta, significa que la API está funcionando correctamente dentro del pod.

---

## 5. **Verificar las Reglas de Firewall**

Asegúrate de que no haya reglas de firewall bloqueando el acceso a la IP externa (`134.33.145.128`) en el puerto **80**.

### a) **Verificar en Azure Portal**

1. Ve al grupo de recursos de tu clúster de AKS en el [Azure Portal](https://portal.azure.com/).
2. Busca el **Load Balancer** asociado a tu clúster.
3. Verifica que las reglas de seguridad permitan el tráfico en el puerto **80**.

---

## 6. **Conclusión**

Si has seguido todos estos pasos y la API aún no responde, es posible que haya un problema en la configuración de la aplicación o en el servicio. Revisa los logs del pod para obtener más detalles y asegúrate de que:

1. El endpoint `/jobs` esté correctamente definido en tu aplicación Flask.
2. El puerto del contenedor (`5000`) coincida con el `targetPort` del servicio.
3. No haya reglas de firewall bloqueando el tráfico.

Si necesitas más ayuda, ¡no dudes en preguntar! 🚀


El error **`/bin/sh: 1: curl: not found`** indica que el comando `curl` no está instalado en el contenedor de tu pod. Esto es común en imágenes de Docker minimalistas (como las basadas en `alpine`), que no incluyen herramientas adicionales para reducir su tamaño.

No te preocupes, hay otras formas de verificar si tu API está funcionando correctamente dentro del pod. Aquí te explico cómo hacerlo:

---

## 1. **Usar `wget` o `nc` (Netcat)**

Algunas imágenes minimalistas incluyen `wget` o `nc` (Netcat). Puedes intentar usar estas herramientas para probar la API.

### a) **Verificar si `wget` está instalado**

Ejecuta:

```bash
wget http://localhost:5000/jobs
```

Si `wget` está instalado, verás una respuesta similar a esta:

```
Connecting to localhost:5000 (127.0.0.1:5000)
saving to 'jobs'
jobs             100% |********************************|   123  0:00:00 ETA
'jobs' saved
```

### b) **Verificar si `nc` (Netcat) está instalado**

Ejecuta:

```bash
nc -zv localhost 5000
```

Si el puerto está abierto, verás algo como esto:

```
Connection to localhost 5000 port [tcp/*] succeeded!
```

---

## 2. **Instalar `curl` en el Contenedor (Opcional)**

Si necesitas `curl` para realizar pruebas más avanzadas, puedes instalarlo temporalmente en el contenedor.

### a) **Acceder al Pod**

Ejecuta un shell dentro del pod:

```bash
kubectl exec -it job-api-576bffc59c-jp5p2 -- /bin/sh
```

### b) **Instalar `curl`**

Dependiendo de la distribución base de tu imagen Docker, usa uno de los siguientes comandos:

- **Si es Alpine Linux**:

  ```bash
  apk add --no-cache curl
  ```

- **Si es Debian/Ubuntu**:

  ```bash
  apt-get update && apt-get install -y curl
  ```

- **Si es CentOS/RHEL**:

  ```bash
  yum install -y curl
  ```

### c) **Probar la API con `curl`**

Una vez instalado `curl`, prueba la API:

```bash
curl http://localhost:5000/jobs
```

---

## 3. **Probar la API desde Fuera del Pod**

Si no puedes instalar `curl` en el contenedor, puedes probar la API desde fuera del pod usando un pod temporal con `curl` instalado.

### a) **Crear un Pod Temporal con `curl`**

Ejecuta el siguiente comando para crear un pod temporal con `curl`:

```bash
kubectl run curl-test --image=curlimages/curl -it --rm -- /bin/sh
```

Esto creará un pod con la imagen `curlimages/curl` y te dará acceso a un shell.

### b) **Probar la API desde el Pod Temporal**

Dentro del pod temporal, usa `curl` para probar la API:

```bash
curl http://job-api-service.default.svc.cluster.local:5000/jobs
```

- **`job-api-service`**: Es el nombre del servicio.
- **`default`**: Es el namespace donde está desplegado el servicio (cámbialo si usas otro namespace).
- **`svc.cluster.local`**: Es el dominio interno de Kubernetes.

---

## 4. **Verificar los Logs del Pod**

Si no puedes acceder a la API, revisa los logs del pod para ver si hay errores:

```bash
kubectl logs job-api-576bffc59c-jp5p2
```

Busca mensajes de error o advertencias que puedan indicar por qué la API no está respondiendo.

---

## 5. **Conclusión**

El error **`curl: not found`** no es un problema grave, ya que puedes usar otras herramientas o instalar `curl` temporalmente en el contenedor. Si la API no responde, revisa los logs del pod para obtener más detalles.

Si necesitas más ayuda, ¡no dudes en preguntar! 🚀



Los logs del pod indican que tu aplicación Flask se está ejecutando en modo **debug** y está escuchando en `http://127.0.0.1:5000`. Esto es un problema, porque Flask solo está escuchando en la interfaz de loopback (`127.0.0.1`), lo que significa que no es accesible desde fuera del pod.

---

## 1. **El Problema**

Flask, por defecto, solo escucha en `127.0.0.1` (localhost). Para que tu API sea accesible desde fuera del pod, Flask debe escuchar en `0.0.0.0`, que significa "todas las interfaces de red".

---

## 2. **Solución**

Debes modificar tu aplicación Flask para que escuche en `0.0.0.0`. Aquí te explico cómo hacerlo:

### a) **Modificar el Código de Flask**

En tu archivo de Flask (por ejemplo, `app.py`), cambia la línea donde inicias la aplicación:

```python
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Escuchar en todas las interfaces
```

### b) **Reconstruir y Subir la Imagen Docker**

1. Reconstruye la imagen Docker:

   ```bash
   docker build -t job-api:latest .
   ```

2. Etiqueta la imagen para subirla al Azure Container Registry (ACR):

   ```bash
   docker tag job-api:latest mycontainerregistrykode.azurecr.io/job-api:latest
   ```

3. Sube la imagen al ACR:

   ```bash
   docker push mycontainerregistrykode.azurecr.io/job-api:latest
   ```

### c) **Actualizar el Deployment en Kubernetes**

Actualiza el deployment para usar la nueva imagen:

```bash
kubectl rollout restart deployment job-api
```

Esto reiniciará los pods con la nueva configuración.

---

## 3. **Verificar que la API Esté Accesible**

Después de reiniciar los pods, verifica que la API esté escuchando en `0.0.0.0`.

### a) **Verificar los Logs del Pod**

Ejecuta:

```bash
kubectl logs <nombre-del-pod>
```

Deberías ver algo como esto:

```
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://0.0.0.0:5000
Press CTRL+C to quit
 * Debugger is active!
 * Debugger PIN: 131-425-827
```

Nota que ahora dice `Running on http://0.0.0.0:5000`, lo que significa que la API está escuchando en todas las interfaces.

### b) **Probar la API desde Fuera del Pod**

Usa la IP externa del servicio (`134.33.145.128`) para acceder a la API:

```bash
curl http://134.33.145.128/jobs
```

Si todo está bien, deberías obtener una respuesta JSON con los trabajos.

---

## 4. **Consideraciones Adicionales**

### a) **Modo de Producción**

El mensaje **`WARNING: This is a development server. Do not use it in a production deployment.`** indica que estás usando el servidor de desarrollo de Flask, que no es adecuado para entornos de producción. Para producción, usa un servidor WSGI como **Gunicorn**.

#### Ejemplo con Gunicorn:

1. Instala Gunicorn en tu Dockerfile:

   ```Dockerfile
   RUN pip install gunicorn
   ```

2. Cambia el comando de inicio en tu Dockerfile:

   ```Dockerfile
   CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
   ```

3. Reconstruye y sube la imagen Docker, luego actualiza el deployment en Kubernetes.

### b) **Configurar HTTPS**

Si tu API es pública, es recomendable configurar HTTPS para proteger las comunicaciones. Puedes usar un **Ingress Controller** en Kubernetes con un certificado SSL/TLS (por ejemplo, de Let's Encrypt).

---

## 5. **Conclusión**

El problema principal era que Flask solo estaba escuchando en `127.0.0.1`. Al cambiarlo a `0.0.0.0`, la API ahora es accesible desde fuera del pod. Si sigues estos pasos, tu API debería funcionar correctamente.

Si necesitas más ayuda para configurar Gunicorn, HTTPS o cualquier otra cosa, ¡no dudes en preguntar! 🚀