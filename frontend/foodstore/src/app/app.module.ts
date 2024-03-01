import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NavigationComponent } from './components/navigation/navigation.component';
import { RegisterPageComponent } from './components/register-page/register-page.component';
import { LoginPageComponent } from './components/login-page/login-page.component';
import { HomePageComponent } from './components/home-page/home-page.component';
import { OwnerHomeComponent } from './components/owner-home/owner-home.component';
import { RegisterRestaurantComponent } from './components/register-restaurant/register-restaurant.component';
import { RestaurantComponent } from './components/restaurant/restaurant.component';
import { AddMenuComponent } from './components/add-menu/add-menu.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatDialogModule } from '@angular/material/dialog';
import { EditMenuFormComponent } from './components/edit-menu-form/edit-menu-form.component';
import { CartComponent } from './components/cart/cart.component';
import { OrderComponent } from './components/order/order.component';
@NgModule({
  declarations: [
    AppComponent,
    NavigationComponent,
    RegisterPageComponent,
    LoginPageComponent,
    HomePageComponent,
    OwnerHomeComponent,
    RegisterRestaurantComponent,
    RestaurantComponent,
    AddMenuComponent,
    EditMenuFormComponent,
    CartComponent,
    OrderComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule ,
    HttpClientModule ,
    FormsModule,
    BrowserAnimationsModule ,
    MatDialogModule ,
  ],  
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
