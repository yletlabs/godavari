import frappe
from frappe.utils import now_datetime

@frappe.whitelist(allow_guest=True)
def get_services():
    return frappe.get_all("Services", fields=["title", "url", "image", "description"])


@frappe.whitelist(allow_guest=True)
def submit_form():
    # Get form data
    data = frappe.form_dict

    # Create a new Contact document
    contact = frappe.get_doc(
        {
            "doctype": "Inquiry",
            "first_name": data.get("first_name"),
            "last_name": data.get("last_name"),
            "email": data.get("email"),
            "phone_number": data.get("phone_number"),
            "message": data.get("message"),
            "creation": now_datetime(),
            "modified": now_datetime(),
        }
    )
    contact.insert(ignore_permissions=True)

    # Return success message
    return {"message": "Form submitted successfully!"}
