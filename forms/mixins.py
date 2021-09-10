
class FormControlMixin:

    def add_form_control_class(self):
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'