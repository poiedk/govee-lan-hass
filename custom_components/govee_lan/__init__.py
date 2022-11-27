""" Govee LAN Control """
from __future__ import annotations

import voluptuous as vol
import logging

from homeassistant.core import HomeAssistant
from homeassistant.components import bluetooth
from homeassistant.helpers.typing import ConfigType
from homeassistant.const import Platform

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)
CONFIG_SCHEMA = vol.Schema({vol.Optional(DOMAIN): {}}, extra=vol.ALLOW_EXTRA)
PLATFORMS: list[Platform] = [Platform.LIGHT]


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    _LOGGER.error("async_setup called!")
    hass.data[DOMAIN] = {}
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up Govee from a config entry."""
    _LOGGER.error("async_setup_entry called! %s", entry.unique_id)
    for component in PLATFORMS:
        hass.async_create_task(
            hass.config_entries.async_forward_entry_setup(entry, component)
        )
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
