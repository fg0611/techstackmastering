
# Guía para Desplegar una Aplicación en Azure Kubernetes Service (AKS)

Este documento describe los pasos necesarios para desplegar una aplicación en Azure Kubernetes Service (AKS), incluyendo la creación de recursos, la configuración de monitoreo, y la gestión de imágenes Docker.

## 1. Instalación de Azure CLI

Primero, instala la CLI de Azure si no la tienes instalada:

```bash
winget install --exact --id Microsoft.AzureCLI
```

---

## 2. Creación de Recursos en Azure

### Crear un Grupo de Recursos

Crea un grupo de recursos en Azure:

```bash
az group create --name myResourceGroup --location eastus
```

### Registrar Proveedores de Servicios

Registra los proveedores de servicios necesarios para el monitoreo y el servicio de contenedores:

```bash
# Registrar el proveedor de monitoreo
az provider register --namespace Microsoft.Insights

# Verificar el estado del registro de monitoreo
az provider show -n Microsoft.Insights --query "registrationState"

# Registrar el proveedor de servicios de contenedores
az provider register --namespace Microsoft.ContainerService

# Verificar el estado del registro de servicios de contenedores
az provider show -n Microsoft.ContainerService --query "registrationState"
```

---

## 3. Creación del Cluster AKS

Crea un cluster de AKS con monitoreo habilitado:

```bash
az aks create --resource-group myResourceGroup --name myAKSCluster --node-count 2 --enable-addons monitoring --generate-ssh-keys
```

### Descargar Credenciales del Cluster

Descarga las credenciales para interactuar con el cluster:

```bash
az aks get-credentials --resource-group myResourceGroup --name myAKSCluster
```

### Verificar Nodos del Cluster

Verifica que los nodos del cluster estén activos:

```bash
kubectl get nodes
```

---

## 4. Construcción y Subida de la Imagen Docker

### Construir la Imagen Docker

Construye la imagen Docker de tu aplicación:

```bash
docker build -t job-api:latest .
```

### Verificar Disponibilidad del Registro de Contenedores

Verifica si el nombre del registro de contenedores está disponible:

```bash
az acr check-name --name mycontainerregistrykode
```

### Crear el Registro de Contenedores

Crea un registro de contenedores en Azure:

```bash
az acr create --resource-group myResourceGroup --name mycontainerregistrykode --sku Basic
```

### Iniciar Sesión en el Registro

Inicia sesión en el registro de contenedores:

```bash
az acr login --name mycontainerregistrykode
```

### Etiquetar y Subir la Imagen

Etiqueta y sube la imagen Docker al registro:

```bash
docker tag job-api:latest mycontainerregistrykode.azurecr.io/job-api:latest
docker push mycontainerregistrykode.azurecr.io/job-api:latest
```

---

## 5. Configuración de Secretos y Base de Datos

### Crear un Secreto para la Conexión a la Base de Datos

Protege la conexión a la base de datos creando un secreto en Kubernetes:

```bash
kubectl create secret generic db-secret --from-literal=DATABASE_URL="postgresql://usuario:contraseña@db-host:5432/job_data"
```

### Generar la Base de Datos

La base de datos puede ser creada en un servicio como **Render** (que utiliza **Neon** y, en última instancia, **Azure**).

---

## 6. Actualización de la Aplicación

### Reconstruir y Subir la Imagen

Si realizas cambios en tu aplicación, reconstruye y sube la imagen actualizada:

```bash
docker build -t mycontainerregistrykode.azurecr.io/job-api:latest .
docker push mycontainerregistrykode.azurecr.io/job-api:latest
```

### Aplicar Cambios en el Deployment

Aplica los cambios en el archivo `deployment.yaml`:

```bash
kubectl apply -f deployment.yaml
```

---

## Conclusión

Con estos pasos, habrás desplegado tu aplicación en Azure Kubernetes Service (AKS) y configurado los recursos necesarios para su funcionamiento. Asegúrate de verificar cada paso para garantizar un despliegue exitoso.
```