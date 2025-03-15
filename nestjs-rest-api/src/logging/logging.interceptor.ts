import {
  Injectable, // 1 se hace inyectable
  NestInterceptor, // 2 se declara como clase interceptor
  ExecutionContext, // 3 se pasa el excution context para obtener datos del request
  CallHandler, // 4 para permitir continuidad ya sea hacia al service o al controller 
} from '@nestjs/common';
import { Observable } from 'rxjs';
import { tap } from 'rxjs/operators';

@Injectable()
export class LoggingInterceptor implements NestInterceptor {
  intercept(context: ExecutionContext, next: CallHandler): Observable<any> {
    console.log("Intercepted ...")
    const now = Date.now()
    return next.handle().pipe(tap(() => console.log(`Took... ${Date.now() - now} ms`)))
  }
}