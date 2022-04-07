import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { LoginScreenComponent } from './login-screen/login-screen.component';

@NgModule({
  imports: [
    RouterModule.forChild([
      {
        path: '',
        component: LoginScreenComponent,
      },
    ]),
  ],
  exports: [RouterModule],
})
export class LoginRoutingModule {}
