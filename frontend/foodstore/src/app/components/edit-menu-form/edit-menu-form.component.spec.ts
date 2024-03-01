import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EditMenuFormComponent } from './edit-menu-form.component';

describe('EditMenuFormComponent', () => {
  let component: EditMenuFormComponent;
  let fixture: ComponentFixture<EditMenuFormComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [EditMenuFormComponent]
    });
    fixture = TestBed.createComponent(EditMenuFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
