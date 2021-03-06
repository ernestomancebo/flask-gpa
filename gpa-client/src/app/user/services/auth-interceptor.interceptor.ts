import {
  HttpEvent,
  HttpHandler,
  HttpInterceptor,
  HttpRequest,
} from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable()
export class AuthInterceptor implements HttpInterceptor {
  constructor() {}

  intercept(
    request: HttpRequest<unknown>,
    next: HttpHandler
  ): Observable<HttpEvent<unknown>> {
    const idToken = localStorage.getItem('id_token');

    if (idToken) {
      const cloned = request.clone({
        headers: request.headers.set('x-access-tokens', idToken),
      });
      return next.handle(cloned);
    } else {
      return next.handle(request);
    }
  }
}
