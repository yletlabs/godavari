import frappe
from frappe import NotFound

def get_context(context):
    context.services = frappe.get_all("Services", fields=["title", "url", "image", "description"])
    service_url = frappe.form_dict.get("service_url")

    service = frappe.get_doc("Services", {"url": service_url})
    if service:
        context.service = service
        context.title = service.title
        context.image = service.image
        context.description = service.description
        context.service_item = service.service_item
    else:
        raise NotFound("Service not found")
