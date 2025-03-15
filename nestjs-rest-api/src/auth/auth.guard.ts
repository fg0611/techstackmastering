import { CanActivate, ExecutionContext, Injectable } from '@nestjs/common';
import { Observable } from 'rxjs';

@Injectable()
export class AuthGuard implements CanActivate {
  canActivate(
    context: ExecutionContext,
  ): boolean | Promise<boolean> | Observable<boolean> {
    // context.switchToHttp(): Este método de ExecutionContext permite acceder al contexto de la solicitud HTTP en sí. 
    // Esto es necesario porque el ExecutionContext
    // también puede ser usado para otros tipos de transportes
    // (como WebSockets, GRPC, etc.), 
    // pero en este caso estamos trabajando con solicitudes HTTP.
    // getRequest(): Este método devuelve el objeto request de
    // Express, lo que te permite acceder a los encabezados,
    // parámetros, cuerpo de la solicitud, etc.
    const request = context.switchToHttp().getRequest() // leer arriba
    // Aquí se obtiene el token de autenticación de los encabezados de la solicitud HTTP.
    // El encabezado Authorization es donde generalmente se envían los tokens (por ejemplo, un JWT) para autenticar al usuario.
    const token = request.headers['authorization']
    const isvalid = token === 'valid-token'
    if (isvalid)
      request.user = { id: 1, name: 'chiqui' }
    return isvalid
  }
}
