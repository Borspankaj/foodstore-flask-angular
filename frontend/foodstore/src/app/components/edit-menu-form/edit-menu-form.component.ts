import { Component } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { MenuService } from 'src/app/services/menu.service';
@Component({
  selector: 'app-edit-menu-form',
  templateUrl: './edit-menu-form.component.html',
  styleUrls: ['./edit-menu-form.component.css']
})
export class EditMenuFormComponent {

  menuId : any
  menu : any 
  errorMessage: string = ''; 
  constructor(
    private route : ActivatedRoute ,
    private menuService : MenuService ,
    private router : Router
  ) {

    this.menuId = this.route.snapshot.paramMap.get('id');
  }

  ngOnInit(){
    this.fetchMenuDetails() ;
  }

  fetchMenuDetails() {
    this.menuService.getMenu(this.menuId).subscribe(
      (data) => {
        this.menu = data;
        console.log(this.menu)
      },
      (error) => {
        console.error('Error fetching book details:', error);
      }
    );
  }

  updateMenu(){
    this.menuService.updateMenu(this.menu).subscribe(
      (data) => {
        
        this.router.navigate(['/owner-home'])
      },
      (error) => {
        this.errorMessage = 'Error adding menu: ' + error.message;
        console.error('Error fetching book details:', error);
      }
    );

  }


}
