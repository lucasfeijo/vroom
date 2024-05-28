import voluptuous as vol
from homeassistant import config_entries

from .const import DOMAIN

@config_entries.HANDLERS.register(DOMAIN)
class VroomConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Vroom."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle vroom's configuration step."""
        if user_input is not None:
            return self.async_create_entry(title="Vroom", data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("email", description="Email"): str,
                vol.Required("vehicle_name", description="Vehicle Name"): str,
            }),
            description_placeholders={
                "email": "Enter the same email configured on the Torque app.",
                "vehicle_name": "Specify a name for the vehicle (used for entities IDs prefix)."
            }
        )
