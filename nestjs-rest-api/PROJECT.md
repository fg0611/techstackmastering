Aquí tienes tu contenido en formato Markdown:

````markdown
# Guía Básica de Nest.js

## Paso 1: Configuración del Proyecto

### Instalar Nest CLI

Si no lo tienes instalado, ejecuta:

```bash
npm install -g @nestjs/cli
```
````

### Crear un nuevo proyecto

```bash
nest new nestjs-rest-api
```

Selecciona el gestor de paquetes que prefieras (npm, yarn o pnpm).

### Ejecutar el proyecto

Navega a la carpeta del proyecto y ejecuta:

```bash
npm run start:dev
```

Esto levantará el servidor en `http://localhost:3000`.

---

## Paso 2: Crear un Módulo Básico

En Nest.js, los módulos son la forma de organizar la aplicación en bloques funcionales.

### Generar un módulo

Ejecuta el siguiente comando para crear un módulo llamado `users`:

```bash
nest generate module users
```

Esto creará una carpeta `users` con un archivo `users.module.ts`.

### Estructura del módulo

Abre `users.module.ts` y verás algo como esto:

```typescript
import { Module } from '@nestjs/common';

@Module({})
export class UsersModule {}
```

El decorador `@Module` define la estructura del módulo.

---

## Paso 3: Crear un Controlador

Los controladores manejan las solicitudes HTTP y definen las rutas de la API.

### Generar un controlador

```bash
nest generate controller users
```

Esto creará un archivo `users.controller.ts` dentro de la carpeta `users`.

### Estructura del controlador

```typescript
import { Controller } from '@nestjs/common';

@Controller('users')
export class UsersController {}
```

El decorador `@Controller('users')` define la ruta base `/users`.

### Agregar un endpoint básico

```typescript
import { Controller, Get } from '@nestjs/common';

@Controller('users')
export class UsersController {
  @Get()
  findAll(): string {
    return 'This action returns all users';
  }
}
```

El decorador `@Get()` define un endpoint GET en `/users`.

### Probar el endpoint

Visita `http://localhost:3000/users` en tu navegador o usa Postman. Deberías ver el mensaje `"This action returns all users"`.

---

## Paso 4: Crear un Servicio

Los servicios contienen la lógica de negocio y son inyectados en los controladores mediante inyección de dependencias.

### Generar un servicio

```bash
nest generate service users
```

Esto creará un archivo `users.service.ts`.

### Estructura del servicio

```typescript
import { Injectable } from '@nestjs/common';

@Injectable()
export class UsersService {}
```

El decorador `@Injectable()` marca la clase como un proveedor.

### Agregar lógica al servicio

```typescript
import { Injectable } from '@nestjs/common';

@Injectable()
export class UsersService {
  private users = [
    { id: 1, name: 'John Doe' },
    { id: 2, name: 'Jane Doe' },
  ];

  findAll() {
    return this.users;
  }
}
```

### Inyectar el servicio en el controlador

Modifica `users.controller.ts`:

```typescript
import { Controller, Get } from '@nestjs/common';
import { UsersService } from './users.service';

@Controller('users')
export class UsersController {
  constructor(private readonly usersService: UsersService) {}

  @Get()
  findAll() {
    return this.usersService.findAll();
  }
}
```

Aquí, el servicio se inyecta en el controlador mediante el constructor.

### Probar el endpoint

Visita `http://localhost:3000/users` nuevamente. Ahora deberías ver la lista de usuarios.

---

## Paso 5: Middleware

Los middleware se ejecutan antes de que una solicitud llegue al controlador.

### Generar un middleware

```bash
nest generate middleware logger
```

Esto creará un archivo `logger.middleware.ts`.

### Implementar el middleware

Abre `logger.middleware.ts`:

```typescript
import { Injectable, NestMiddleware } from '@nestjs/common';
import { Request, Response, NextFunction } from 'express';

@Injectable()
export class LoggerMiddleware implements NestMiddleware {
  use(req: Request, res: Response, next: NextFunction) {
    console.log('Request...');
    next();
  }
}
```

### Registrar el middleware

Abre `users.module.ts` y regístralo:

```typescript
import { Module, MiddlewareConsumer } from '@nestjs/common';
import { UsersController } from './users.controller';
import { UsersService } from './users.service';
import { LoggerMiddleware } from './logger.middleware';

@Module({
  controllers: [UsersController],
  providers: [UsersService],
})
export class UsersModule {
  configure(consumer: MiddlewareConsumer) {
    consumer.apply(LoggerMiddleware).forRoutes('users');
  }
}
```

### Probar el middleware

Visita `http://localhost:3000/users` y revisa la consola. Deberías ver el mensaje `"Request..."`.

---

## Resumen hasta ahora

Hemos cubierto:

- **Módulos (`@Module`)**
- **Controladores (`@Controller`, `@Get`)**
- **Servicios (`@Injectable`, inyección de dependencias)**
- **Middleware (`NestMiddleware`)**

```

```
