import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ArrowBallComponent } from './arrow-ball.component';

describe('ArrowBallComponent', () => {
  let component: ArrowBallComponent;
  let fixture: ComponentFixture<ArrowBallComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ArrowBallComponent]
    });
    fixture = TestBed.createComponent(ArrowBallComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
