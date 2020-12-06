import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { BarGraphNnpComponent } from './bar-graph-nnp.component';

describe('BarGraphNnpComponent', () => {
  let component: BarGraphNnpComponent;
  let fixture: ComponentFixture<BarGraphNnpComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ BarGraphNnpComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(BarGraphNnpComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
