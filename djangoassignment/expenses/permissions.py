from rest_framework.permissions import BasePermission

class ExpenseUpdatePermission(BasePermission):

    '''this permission defines only for the user who created it.'''

    def has_object_permission(self,request,view,object):

        return object.created_by==request.user