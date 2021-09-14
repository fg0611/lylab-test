import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { HomeComponent } from './home/home.component';
import { CreditsComponent } from './credits/credits.component';
import { ClientsComponent } from './clients/clients.component';

const routes: Routes = [
  { path: 'home', component: HomeComponent },
  { path: 'credits', component: CreditsComponent },
  { path: 'clients', component: ClientsComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
