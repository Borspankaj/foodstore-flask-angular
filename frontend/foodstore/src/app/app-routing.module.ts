import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { RegisterPageComponent } from './components/register-page/register-page.component';
import { LoginPageComponent } from './components/login-page/login-page.component';
import { HomePageComponent } from './components/home-page/home-page.component';
import { RestaurantComponent } from './components/restaurant/restaurant.component';
import { OwnerHomeComponent } from './components/owner-home/owner-home.component';
import { RegisterRestaurantComponent } from './components/register-restaurant/register-restaurant.component';
import { AddMenuComponent } from './components/add-menu/add-menu.component';
import { EditMenuFormComponent } from './components/edit-menu-form/edit-menu-form.component';
import { CartComponent } from './components/cart/cart.component';
import { OrderComponent } from './components/order/order.component';
const routes: Routes = [
  { path : 'register-user' , component : RegisterPageComponent } ,
  { path : '' , component : LoginPageComponent } ,
  { path : 'login' , component : LoginPageComponent} ,
  { path : 'home' , component : HomePageComponent } ,
  { path : 'restaurant/:id', component: RestaurantComponent } ,
  { path : 'owner-home', component: OwnerHomeComponent } ,
  { path : 'register-restaurant' , component : RegisterRestaurantComponent} ,
  { path : 'add-menu/:id' , component : AddMenuComponent } ,
  { path : 'edit-menu/:id' , component : EditMenuFormComponent} ,
  { path : 'mycart' , component : CartComponent } ,
  { path : 'myorders' , component : OrderComponent} ,

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
