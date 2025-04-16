import frappe

def get_context(context):
    context.user = frappe.session.user
    context.services = frappe.get_all("Services", fields=["title", "url", "image", "description"])
    return context