import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { MenuService } from 'src/app/services/menu.service';
import { Router } from '@angular/router';
import { throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';

@Component({
  selector: 'app-add-menu',
  templateUrl: './add-menu.component.html',
  styleUrls: ['./add-menu.component.css']
})
export class AddMenuComponent {
  restaurantId: any;
  menu = {
    dishName: '',
    price: '',
    description: ''
  };

  errorMessage: string = ''; 

  constructor(
    private route: ActivatedRoute,
    private menuService: MenuService,
    private router: Router
  ) {
    this.restaurantId = this.route.snapshot.paramMap.get('id');
  }

  submitForm() {
    this.menuService.addMenu(this.menu, this.restaurantId).pipe(
      catchError((error) => {
        this.errorMessage = 'Error adding menu: ' + error.message;
        return throwError(error);
      })
    ).subscribe(
      (response) => {
        console.log('Menu added successfully:', response);
        this.router.navigate(['/owner-home']);
      },
      (error) => {
        console.error('Error adding menu:', error);
        this.errorMessage = 'Error adding menu: ' + error.message;
      }
    );
  }
}
