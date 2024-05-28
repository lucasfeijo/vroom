"""Vroom is a Torque compatible integration."""

from homeassistant.helpers import config_validation as cv

from .const import DOMAIN

async def async_setup(hass, config):
    return True

async def async_setup_entry(hass, entry):
    hass.async_add_job(hass.config_entries.async_forward_entry_setup(entry, "sensor"))
    return True

async def async_unload_entry(hass, entry):
    await hass.config_entries.async_forward_entry_unload(entry, "sensor")
    return True