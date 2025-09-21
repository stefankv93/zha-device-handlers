"""Aqara led strip T1."""

from typing import Final

from zigpy import types as t
from zigpy.quirks.v2 import QuirkBuilder
from zigpy.quirks.v2.homeassistant import PERCENTAGE, UnitOfLength
from zigpy.zcl.foundation import DataTypeId, ZCLAttributeDef

from zhaquirks.xiaomi import XiaomiAqaraE1Cluster


class LedStripT1PowerOnStateMode(t.enum8):
    """Aqara led strip power on state."""

    On = 0x00
    Previous = 0x01
    Off = 0x02
    Toggle = 0x03


class LedStripT1Audio(t.enum8):
    """Aqara led strip audio enabled."""

    Off = 0x00
    On = 0x01


class LedStripT1AudioSensitivity(t.enum8):
    "Aqara led strip audio sensitivity."

    Low = 0x00
    Medium = 0x01
    High = 0x02


class LedStripT1AudioEffect(t.enum32):
    "Aqara led strip audio effect."

    Random = 0x00
    Blink = 0x01
    Rainbow = 0x02
    Wave = 0x03

class LedStripT1Preset(t.enum32):
    "Aqara led strip preset."

    Breathe = 0x00
    Rainbow = 0x01
    Sweep = 0x02
    Flashing = 0x03
    Strobe = 0x04
    ReversedRainbow = 0x05
    Colorful = 0x06
    Scan = 0x07

MIN_BRIGHTNESS_ID = 0x0515
MAX_BRIGHTNESS_ID = 0x0516
POWER_ON_STATE_ID = 0x0517
STRIP_LENGTH_ID = 0x051B
ENABLE_AUDIO_ID = 0x051C
AUDIO_EFECT_ID = 0x051D
AUDIO_SENSITIVITY_ID = 0x051E
PRESET_ID = 0x051F
SPEED_ID = 0x0520


class AqaraLedStripT1(XiaomiAqaraE1Cluster):
    """Opple cluster."""

    class AttributeDefs(XiaomiAqaraE1Cluster.AttributeDefs):
        """Attribute definitions."""

        min_brightness: Final = ZCLAttributeDef(
            id=MIN_BRIGHTNESS_ID, type=t.uint8_t, is_manufacturer_specific=True
        )

        max_brightness: Final = ZCLAttributeDef(
            id=MAX_BRIGHTNESS_ID, type=t.uint8_t, is_manufacturer_specific=True
        )

        power_on_state: Final = ZCLAttributeDef(
            id=POWER_ON_STATE_ID,
            type=LedStripT1PowerOnStateMode,
            zcl_type=DataTypeId.uint8,
            is_manufacturer_specific=True,
        )

        length: Final = ZCLAttributeDef(
            id=STRIP_LENGTH_ID, type=t.uint8_t, is_manufacturer_specific=True
        )

        audio: Final = ZCLAttributeDef(
            id=ENABLE_AUDIO_ID,
            type=LedStripT1Audio,
            zcl_type=DataTypeId.uint8,
            is_manufacturer_specific=True,
        )

        audio_sensitivity: Final = ZCLAttributeDef(
            id=AUDIO_SENSITIVITY_ID,
            type=LedStripT1AudioSensitivity,
            zcl_type=DataTypeId.uint8,
            is_manufacturer_specific=True,
        )

        audio_effect: Final = ZCLAttributeDef(
            id=AUDIO_EFECT_ID,
            type=LedStripT1AudioEffect,
            zcl_type=DataTypeId.uint32,
            is_manufacturer_specific=True,
        )

        preset: Final = ZCLAttributeDef(
            id=PRESET_ID, 
            type=LedStripT1Preset, 
            zcl_type=DataTypeId.uint32, 
            is_manufacturer_specific=True
        )

        speed: Final = ZCLAttributeDef(
            id=SPEED_ID, type=t.uint8_t, is_manufacturer_specific=True
        )


(
    QuirkBuilder("Aqara", "lumi.light.acn132")
    .friendly_name(manufacturer="Aqara", model="Led strip T1")
    .replaces(AqaraLedStripT1)
    .number(
        AqaraLedStripT1.AttributeDefs.min_brightness.name,
        AqaraLedStripT1.cluster_id,
        min_value=0,
        max_value=99,
        step=1.0,
        unit=PERCENTAGE,
        translation_key="min_brightness",
        fallback_name="Minimum brightness",
    )
    .number(
        AqaraLedStripT1.AttributeDefs.max_brightness.name,
        AqaraLedStripT1.cluster_id,
        min_value=0,
        max_value=99,
        step=1.0,
        unit=PERCENTAGE,
        translation_key="max_brightness",
        fallback_name="Maximum brightness",
    )
    .enum(
        AqaraLedStripT1.AttributeDefs.power_on_state.name,
        LedStripT1PowerOnStateMode,
        AqaraLedStripT1.cluster_id,
        translation_key="power_on_state",
        fallback_name="Power on state",
    )
    .number(
        AqaraLedStripT1.AttributeDefs.length.name,
        AqaraLedStripT1.cluster_id,
        min_value=1,
        max_value=10,
        step=0.2,
        multiplier=0.2,
        unit=UnitOfLength.METERS,
        translation_key="length",
        fallback_name="Length",
    )
    .enum(
        AqaraLedStripT1.AttributeDefs.audio.name,
        LedStripT1Audio,
        AqaraLedStripT1.cluster_id,
        translation_key="audio",
        fallback_name="Audio",
    )
    .enum(
        AqaraLedStripT1.AttributeDefs.audio_sensitivity.name,
        LedStripT1AudioSensitivity,
        AqaraLedStripT1.cluster_id,
        translation_key="audio_sensitivity",
        fallback_name="Audio sensitivity",
    )
    .enum(
        AqaraLedStripT1.AttributeDefs.audio_effect.name,
        LedStripT1AudioEffect,
        AqaraLedStripT1.cluster_id,
        translation_key="audio_effect",
        fallback_name="Audio effect",
    )
    .enum(
        AqaraLedStripT1.AttributeDefs.preset.name,
        LedStripT1Preset,
        AqaraLedStripT1.cluster_id,
        translation_key="preset",
        fallback_name="Preset",
    )
    .number(
        AqaraLedStripT1.AttributeDefs.speed.name,
        AqaraLedStripT1.cluster_id,
        min_value=1,
        max_value=100,
        step=1,
        translation_key="speed",
        fallback_name="Speed",
    )
    .add_to_registry()
)
