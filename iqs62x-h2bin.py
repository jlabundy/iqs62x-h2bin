#!/usr/bin/env python3

"""
iqs62x-h2bin.py: Header file converter for six-channel Azoteq ProxFusion
                 devices (IQS620A, IQS621, IQS622, IQS624 and IQS625).
"""

import datetime
import sys

MAP_NONE = 0
MAP_BOTH = 1
MAP_PROX = 2
MAP_SAR1 = 3

field_map = {}

# IQS620A --------------------------------------------------------------------

field_map[('IQS620A', 'PXS_SETTINGS0_0')]           = (0x40, 0xFF, MAP_BOTH)
field_map[('IQS620A', 'PXS_SETTINGS0_1')]           = (0x41, 0xFF, MAP_BOTH)
field_map[('IQS620A', 'PXS_SETTINGS0_2')]           = (0x42, 0xFF, MAP_BOTH)
field_map[('IQS620A', 'PXS_SETTINGS0_3')]           = (0x43, 0xFF, MAP_BOTH)
field_map[('IQS620A', 'PXS_SETTINGS0_4')]           = (0x44, 0xFF, MAP_BOTH)
field_map[('IQS620A', 'PXS_SETTINGS0_5')]           = (0x45, 0xFF, MAP_BOTH)
field_map[('IQS620A', 'PXS_SETTINGS0_6')]           = (0x46, 0xFF, MAP_BOTH)
field_map[('IQS620A', 'PXS_SETTINGS0_7')]           = (0x47, 0xFF, MAP_BOTH)
field_map[('IQS620A', 'PXS_SETTINGS0_8')]           = (0x48, 0xFF, MAP_BOTH)
field_map[('IQS620A', 'PXS_SETTINGS0_9')]           = (0x49, 0xFF, MAP_BOTH)
field_map[('IQS620A', 'PXS_SETTINGS0_10')]          = (0x4A, 0xFF, MAP_BOTH)
field_map[('IQS620A', 'PXS_SETTINGS0_11')]          = (0x4B, 0xFF, MAP_BOTH)

field_map[('IQS620A', 'PXS_SETTINGS1_0')]           = (0x50, 0xFF, MAP_BOTH)
field_map[('IQS620A', 'PXS_SETTINGS1_1')]           = (0x51, 0xFF, MAP_BOTH)
field_map[('IQS620A', 'PXS_SETTINGS1_2')]           = (0x52, 0xFF, MAP_BOTH)
field_map[('IQS620A', 'PXS_SETTINGS1_3')]           = (0x53, 0xFF, MAP_BOTH)
field_map[('IQS620A', 'PXS_SETTINGS1_4')]           = (0x54, 0xFF, MAP_BOTH)
field_map[('IQS620A', 'PXS_SETTINGS1_5')]           = (0x55, 0xFF, MAP_BOTH)
field_map[('IQS620A', 'PXS_SETTINGS1_6')]           = (0x56, 0xFF, MAP_BOTH)
field_map[('IQS620A', 'PXS_SETTINGS1_7')]           = (0x57, 0xFF, MAP_BOTH)

field_map[('IQS620A', 'PXS_UI_SETTINGS_0')]         = (0x60, 0xFF, MAP_PROX)
field_map[('IQS620A', 'PXS_UI_SETTINGS_1')]         = (0x61, 0xFF, MAP_PROX)
field_map[('IQS620A', 'PXS_UI_SETTINGS_2')]         = (0x62, 0xFF, MAP_PROX)
field_map[('IQS620A', 'PXS_UI_SETTINGS_3')]         = (0x63, 0xFF, MAP_PROX)
field_map[('IQS620A', 'PXS_UI_SETTINGS_4')]         = (0x64, 0xFF, MAP_PROX)
field_map[('IQS620A', 'PXS_UI_SETTINGS_5')]         = (0x65, 0xFF, MAP_PROX)
field_map[('IQS620A', 'PXS_UI_SETTINGS_6')]         = (0x66, 0xFF, MAP_PROX)

field_map[('IQS620A', 'SAR_UI_SETTINGS_0')]         = (0x70, 0xF7, MAP_SAR1)
field_map[('IQS620A', 'SAR_UI_SETTINGS_1')]         = (0x71, 0xFF, MAP_SAR1)
field_map[('IQS620A', 'SAR_UI_SETTINGS_2')]         = (0x72, 0xFF, MAP_SAR1)
field_map[('IQS620A', 'SAR_UI_SETTINGS_3')]         = (0x73, 0xFF, MAP_SAR1)
field_map[('IQS620A', 'SAR_UI_SETTINGS_4')]         = (0x74, 0xFF, MAP_SAR1)
field_map[('IQS620A', 'SAR_UI_SETTINGS_5')]         = (0x75, 0xFF, MAP_SAR1)

field_map[('IQS620A', 'HYSTERESIS_UI_SETTINGS_0')]  = (0x80, 0xFF, MAP_BOTH)
field_map[('IQS620A', 'HYSTERESIS_UI_SETTINGS_1')]  = (0x81, 0xFF, MAP_BOTH)
field_map[('IQS620A', 'HYSTERESIS_UI_SETTINGS_2')]  = (0x82, 0xFF, MAP_BOTH)
field_map[('IQS620A', 'HYSTERESIS_UI_SETTINGS_3')]  = (0x83, 0xFF, MAP_BOTH)

field_map[('IQS620A', 'HALL_SENSOR_SETTINGS_0')]    = (0x90, 0xFF, MAP_BOTH)
field_map[('IQS620A', 'HALL_SENSOR_SETTINGS_1')]    = (0x91, 0xFF, MAP_BOTH)
field_map[('IQS620A', 'HALL_SENSOR_SETTINGS_2')]    = (0x92, 0xFF, MAP_BOTH)
field_map[('IQS620A', 'HALL_SENSOR_SETTINGS_3')]    = (0x93, 0xFF, MAP_BOTH)

field_map[('IQS620A', 'HALL_UI_SETTINGS_0')]        = (0xA0, 0xFF, MAP_BOTH)
field_map[('IQS620A', 'HALL_UI_SETTINGS_1')]        = (0xA1, 0xFF, MAP_BOTH)
field_map[('IQS620A', 'HALL_UI_SETTINGS_2')]        = (0xA2, 0xFF, MAP_BOTH)

field_map[('IQS620A', 'TEMP_UI_SETTINGS_0')]        = (0xC0, 0xFF, MAP_BOTH)
field_map[('IQS620A', 'TEMP_UI_SETTINGS_1')]        = (0xC1, 0x00, MAP_BOTH)
field_map[('IQS620A', 'TEMP_UI_SETTINGS_2')]        = (0xC2, 0x00, MAP_BOTH)
field_map[('IQS620A', 'TEMP_UI_SETTINGS_3')]        = (0xC3, 0x00, MAP_BOTH)
field_map[('IQS620A', 'TEMP_UI_SETTINGS_4')]        = (0xC4, 0x00, MAP_BOTH)

field_map[('IQS620A', 'SYSTEM_SETTINGS')]           = (0xD0, 0x1C, MAP_BOTH)
field_map[('IQS620A', 'ACTIVE_CHS')]                = (0xD1, 0xFF, MAP_BOTH)
field_map[('IQS620A', 'PMU_SETTINGS')]              = (0xD2, 0x00, MAP_BOTH)
field_map[('IQS620A', 'REPORT_RATES_TIMINGS_0')]    = (0xD3, 0xFF, MAP_BOTH)
field_map[('IQS620A', 'REPORT_RATES_TIMINGS_1')]    = (0xD4, 0xFF, MAP_BOTH)
field_map[('IQS620A', 'REPORT_RATES_TIMINGS_2')]    = (0xD5, 0xFF, MAP_BOTH)
field_map[('IQS620A', 'REPORT_RATES_TIMINGS_3')]    = (0xD6, 0xFF, MAP_BOTH)
field_map[('IQS620A', 'GLOBAL_EVENT_MASK')]         = (0xD7, 0x00, MAP_BOTH)
field_map[('IQS620A', 'PWM_DUTY_CYCLE')]            = (0xD8, 0x00, MAP_BOTH)
field_map[('IQS620A', 'RDY_TIMEOUT_PERIOD')]        = (0xD9, 0x00, MAP_BOTH)
field_map[('IQS620A', 'I2C_SETTINGS')]              = (0xDA, 0x00, MAP_BOTH)
field_map[('IQS620A', 'CH_RESEED_ENABLE')]          = (0xDB, 0xFF, MAP_BOTH)

# IQS621 ---------------------------------------------------------------------

field_map[('IQS621', 'PXS_SETTINGS_0')]             = (0x40, 0xFF, MAP_BOTH)
field_map[('IQS621', 'PXS_SETTINGS_1')]             = (0x41, 0xFF, MAP_BOTH)
field_map[('IQS621', 'PXS_SETTINGS_2')]             = (0x42, 0xFF, MAP_BOTH)
field_map[('IQS621', 'PXS_SETTINGS_3')]             = (0x43, 0xFF, MAP_BOTH)
field_map[('IQS621', 'PXS_SETTINGS_4')]             = (0x44, 0xFF, MAP_BOTH)
field_map[('IQS621', 'PXS_SETTINGS_5')]             = (0x45, 0xFF, MAP_BOTH)
field_map[('IQS621', 'PXS_SETTINGS_6')]             = (0x46, 0xFF, MAP_BOTH)
field_map[('IQS621', 'PXS_SETTINGS_7')]             = (0x47, 0xFF, MAP_BOTH)
field_map[('IQS621', 'PXS_SETTINGS_8')]             = (0x48, 0xFF, MAP_BOTH)
field_map[('IQS621', 'PXS_SETTINGS_9')]             = (0x49, 0xFF, MAP_BOTH)
field_map[('IQS621', 'PXS_SETTINGS_10')]            = (0x4A, 0xFF, MAP_BOTH)
field_map[('IQS621', 'PXS_SETTINGS_11')]            = (0x4B, 0xFF, MAP_BOTH)
field_map[('IQS621', 'PXS_SETTINGS_12')]            = (0x4C, 0xFF, MAP_BOTH)
field_map[('IQS621', 'PXS_SETTINGS_13')]            = (0x4D, 0xFF, MAP_BOTH)

field_map[('IQS621', 'PXS_UI_SETTINGS_0')]          = (0x50, 0xFF, MAP_BOTH)
field_map[('IQS621', 'PXS_UI_SETTINGS_1')]          = (0x51, 0xFF, MAP_BOTH)
field_map[('IQS621', 'PXS_UI_SETTINGS_2')]          = (0x52, 0xFF, MAP_BOTH)
field_map[('IQS621', 'PXS_UI_SETTINGS_3')]          = (0x53, 0xFF, MAP_BOTH)
field_map[('IQS621', 'PXS_UI_SETTINGS_4')]          = (0x54, 0xFF, MAP_BOTH)

field_map[('IQS621', 'METAL_UI_SETTINGS_0')]        = (0x60, 0xFF, MAP_BOTH)
field_map[('IQS621', 'METAL_UI_SETTINGS_1')]        = (0x61, 0xFF, MAP_BOTH)
field_map[('IQS621', 'METAL_UI_SETTINGS_2')]        = (0x62, 0xFF, MAP_BOTH)
field_map[('IQS621', 'METAL_UI_SETTINGS_3')]        = (0x63, 0xFF, MAP_BOTH)

field_map[('IQS621', 'LIGHT_SENSOR_SETTINGS_0')]    = (0x70, 0xFF, MAP_BOTH)
field_map[('IQS621', 'LIGHT_SENSOR_SETTINGS_1')]    = (0x71, 0xFC, MAP_BOTH)
field_map[('IQS621', 'LIGHT_SENSOR_SETTINGS_2')]    = (0x72, 0xFF, MAP_BOTH)
field_map[('IQS621', 'LIGHT_SENSOR_SETTINGS_3')]    = (0x73, 0xFF, MAP_BOTH)

field_map[('IQS621', 'ALS_UI_SETTINGS_0')]          = (0x80, 0xFF, MAP_BOTH)
field_map[('IQS621', 'ALS_UI_SETTINGS_1')]          = (0x81, 0xFF, MAP_BOTH)
field_map[('IQS621', 'ALS_UI_SETTINGS_2')]          = (0x82, 0x00, MAP_BOTH)
field_map[('IQS621', 'ALS_UI_SETTINGS_3')]          = (0x83, 0x00, MAP_BOTH)

field_map[('IQS621', 'HALL_SENSOR_SETTINGS_0')]     = (0x90, 0xFF, MAP_BOTH)
field_map[('IQS621', 'HALL_SENSOR_SETTINGS_1')]     = (0x91, 0xFF, MAP_BOTH)
field_map[('IQS621', 'HALL_SENSOR_SETTINGS_2')]     = (0x92, 0xFF, MAP_BOTH)
field_map[('IQS621', 'HALL_SENSOR_SETTINGS_3')]     = (0x93, 0xFF, MAP_BOTH)

field_map[('IQS621', 'HALL_UI_SETTINGS_0')]         = (0xA0, 0xFF, MAP_BOTH)
field_map[('IQS621', 'HALL_UI_SETTINGS_1')]         = (0xA1, 0xFF, MAP_BOTH)
field_map[('IQS621', 'HALL_UI_SETTINGS_2')]         = (0xA2, 0xFF, MAP_BOTH)

field_map[('IQS621', 'TEMP_UI_SETTINGS_0')]         = (0xC0, 0xFF, MAP_BOTH)
field_map[('IQS621', 'TEMP_UI_SETTINGS_1')]         = (0xC1, 0xFF, MAP_BOTH)
field_map[('IQS621', 'TEMP_UI_SETTINGS_2')]         = (0xC2, 0xFF, MAP_BOTH)
field_map[('IQS621', 'TEMP_UI_SETTINGS_3')]         = (0xC3, 0xFF, MAP_BOTH)

field_map[('IQS621', 'SYSTEM_SETTINGS')]            = (0xD0, 0x1C, MAP_BOTH)
field_map[('IQS621', 'ACTIVE_CHS')]                 = (0xD1, 0xFF, MAP_BOTH)
field_map[('IQS621', 'PMU_SETTINGS')]               = (0xD2, 0x00, MAP_BOTH)
field_map[('IQS621', 'REPORT_RATES_TIMINGS_0')]     = (0xD3, 0xFF, MAP_BOTH)
field_map[('IQS621', 'REPORT_RATES_TIMINGS_1')]     = (0xD4, 0xFF, MAP_BOTH)
field_map[('IQS621', 'REPORT_RATES_TIMINGS_2')]     = (0xD5, 0xFF, MAP_BOTH)
field_map[('IQS621', 'REPORT_RATES_TIMINGS_3')]     = (0xD6, 0xFF, MAP_BOTH)
field_map[('IQS621', 'GLOBAL_EVENT_MASK')]          = (0xD7, 0x00, MAP_BOTH)
field_map[('IQS621', 'RDY_TIMEOUT_PERIOD')]         = (0xD8, 0x00, MAP_BOTH)
field_map[('IQS621', 'I2C_SETTINGS')]               = (0xD9, 0x00, MAP_BOTH)

# IQS622 ---------------------------------------------------------------------

field_map[('IQS622', 'PXS_SETTINGS_0')]             = (0x40, 0xFF, MAP_BOTH)
field_map[('IQS622', 'PXS_SETTINGS_1')]             = (0x41, 0xFF, MAP_BOTH)
field_map[('IQS622', 'PXS_SETTINGS_2')]             = (0x42, 0xFF, MAP_BOTH)
field_map[('IQS622', 'PXS_SETTINGS_3')]             = (0x43, 0xFF, MAP_BOTH)
field_map[('IQS622', 'PXS_SETTINGS_4')]             = (0x44, 0xFF, MAP_BOTH)
field_map[('IQS622', 'PXS_SETTINGS_5')]             = (0x45, 0xFF, MAP_BOTH)
field_map[('IQS622', 'PXS_SETTINGS_6')]             = (0x46, 0xFF, MAP_BOTH)
field_map[('IQS622', 'PXS_SETTINGS_7')]             = (0x47, 0xFF, MAP_BOTH)
field_map[('IQS622', 'PXS_SETTINGS_8')]             = (0x48, 0xFF, MAP_BOTH)
field_map[('IQS622', 'PXS_SETTINGS_9')]             = (0x49, 0xFF, MAP_BOTH)
field_map[('IQS622', 'PXS_SETTINGS_10')]            = (0x4A, 0xFF, MAP_BOTH)
field_map[('IQS622', 'PXS_SETTINGS_11')]            = (0x4B, 0xFF, MAP_BOTH)
field_map[('IQS622', 'PXS_SETTINGS_12')]            = (0x4C, 0xFF, MAP_BOTH)
field_map[('IQS622', 'PXS_SETTINGS_13')]            = (0x4D, 0xFF, MAP_BOTH)

field_map[('IQS622', 'PXS_UI_SETTINGS_0')]          = (0x50, 0xFF, MAP_PROX)
field_map[('IQS622', 'PXS_UI_SETTINGS_1')]          = (0x51, 0xFF, MAP_PROX)
field_map[('IQS622', 'PXS_UI_SETTINGS_2')]          = (0x52, 0xFF, MAP_PROX)
field_map[('IQS622', 'PXS_UI_SETTINGS_3')]          = (0x53, 0xFF, MAP_PROX)
field_map[('IQS622', 'PXS_UI_SETTINGS_4')]          = (0x54, 0xFF, MAP_PROX)

field_map[('IQS622', 'SAR_UI_SETTINGS_0')]          = (0x60, 0xFF, MAP_SAR1)
field_map[('IQS622', 'SAR_UI_SETTINGS_1')]          = (0x61, 0xFF, MAP_SAR1)
field_map[('IQS622', 'SAR_UI_SETTINGS_2')]          = (0x62, 0xFF, MAP_SAR1)
field_map[('IQS622', 'SAR_UI_SETTINGS_3')]          = (0x63, 0xFF, MAP_SAR1)
field_map[('IQS622', 'SAR_UI_SETTINGS_4')]          = (0x64, 0xFF, MAP_SAR1)
field_map[('IQS622', 'SAR_UI_SETTINGS_5')]          = (0x65, 0xFF, MAP_SAR1)

field_map[('IQS622', 'LIGHT_SENSOR_SETTINGS_0')]    = (0x70, 0xFF, MAP_BOTH)
field_map[('IQS622', 'LIGHT_SENSOR_SETTINGS_1')]    = (0x71, 0xFC, MAP_BOTH)
field_map[('IQS622', 'LIGHT_SENSOR_SETTINGS_2')]    = (0x72, 0xFF, MAP_BOTH)
field_map[('IQS622', 'LIGHT_SENSOR_SETTINGS_3')]    = (0x73, 0xFC, MAP_BOTH)
field_map[('IQS622', 'LIGHT_SENSOR_SETTINGS_4')]    = (0x74, 0xFF, MAP_BOTH)
field_map[('IQS622', 'LIGHT_SENSOR_SETTINGS_5')]    = (0x75, 0xFF, MAP_BOTH)

field_map[('IQS622', 'IR_UI_SETTINGS_0')]           = (0x90, 0xFF, MAP_BOTH)
field_map[('IQS622', 'IR_UI_SETTINGS_1')]           = (0x91, 0xFF, MAP_BOTH)
field_map[('IQS622', 'IR_UI_SETTINGS_2')]           = (0x92, 0xFF, MAP_BOTH)
field_map[('IQS622', 'IR_UI_SETTINGS_3')]           = (0x93, 0xFF, MAP_BOTH)

field_map[('IQS622', 'HALL_SENSOR_SETTINGS_0')]     = (0xA0, 0xFF, MAP_BOTH)
field_map[('IQS622', 'HALL_SENSOR_SETTINGS_1')]     = (0xA1, 0xFF, MAP_BOTH)
field_map[('IQS622', 'HALL_SENSOR_SETTINGS_2')]     = (0xA2, 0xFF, MAP_BOTH)
field_map[('IQS622', 'HALL_SENSOR_SETTINGS_3')]     = (0xA3, 0xFF, MAP_BOTH)

field_map[('IQS622', 'HALL_UI_SETTINGS_0')]         = (0xB0, 0xFF, MAP_BOTH)
field_map[('IQS622', 'HALL_UI_SETTINGS_1')]         = (0xB1, 0xFF, MAP_BOTH)
field_map[('IQS622', 'HALL_UI_SETTINGS_2')]         = (0xB2, 0xFF, MAP_BOTH)

field_map[('IQS622', 'SYSTEM_SETTINGS')]            = (0xD0, 0x1C, MAP_BOTH)
field_map[('IQS622', 'ACTIVE_CHS')]                 = (0xD1, 0xFF, MAP_BOTH)
field_map[('IQS622', 'PMU_SETTINGS')]               = (0xD2, 0x00, MAP_BOTH)
field_map[('IQS622', 'REPORT_RATES_TIMINGS_0')]     = (0xD3, 0xFF, MAP_BOTH)
field_map[('IQS622', 'REPORT_RATES_TIMINGS_1')]     = (0xD4, 0xFF, MAP_BOTH)
field_map[('IQS622', 'REPORT_RATES_TIMINGS_2')]     = (0xD5, 0xFF, MAP_BOTH)
field_map[('IQS622', 'REPORT_RATES_TIMINGS_3')]     = (0xD6, 0xFF, MAP_BOTH)
field_map[('IQS622', 'GLOBAL_EVENT_MASK')]          = (0xD7, 0x00, MAP_BOTH)

# IQS624 ---------------------------------------------------------------------

field_map[('IQS624', 'PXS_SETTINGS_0')]             = (0x40, 0xFF, MAP_BOTH)
field_map[('IQS624', 'PXS_SETTINGS_1')]             = (0x41, 0xFF, MAP_BOTH)
field_map[('IQS624', 'PXS_SETTINGS_2')]             = (0x42, 0xFF, MAP_BOTH)
field_map[('IQS624', 'PXS_SETTINGS_3')]             = (0x43, 0xFF, MAP_BOTH)
field_map[('IQS624', 'PXS_SETTINGS_4')]             = (0x44, 0xFF, MAP_BOTH)
field_map[('IQS624', 'PXS_SETTINGS_5')]             = (0x45, 0xFF, MAP_BOTH)
field_map[('IQS624', 'PXS_SETTINGS_6')]             = (0x46, 0xFF, MAP_BOTH)
field_map[('IQS624', 'PXS_SETTINGS_7')]             = (0x47, 0xFF, MAP_BOTH)
field_map[('IQS624', 'PXS_SETTINGS_8')]             = (0x48, 0xFF, MAP_BOTH)
field_map[('IQS624', 'PXS_SETTINGS_9')]             = (0x49, 0xFF, MAP_BOTH)

field_map[('IQS624', 'PXS_UI_SETTINGS_0')]          = (0x50, 0xFF, MAP_BOTH)
field_map[('IQS624', 'PXS_UI_SETTINGS_1')]          = (0x51, 0xFF, MAP_BOTH)
field_map[('IQS624', 'PXS_UI_SETTINGS_2')]          = (0x52, 0xFF, MAP_BOTH)
field_map[('IQS624', 'PXS_UI_SETTINGS_3')]          = (0x53, 0xFF, MAP_BOTH)
field_map[('IQS624', 'PXS_UI_SETTINGS_4')]          = (0x54, 0xFF, MAP_BOTH)

field_map[('IQS624', 'HALL_SETTINGS_0')]            = (0x70, 0x00, MAP_BOTH)
field_map[('IQS624', 'HALL_SETTINGS_1')]            = (0x71, 0xFF, MAP_BOTH)
field_map[('IQS624', 'HALL_SETTINGS_2')]            = (0x72, 0x00, MAP_BOTH)
field_map[('IQS624', 'HALL_SETTINGS_3')]            = (0x73, 0x00, MAP_BOTH)
field_map[('IQS624', 'HALL_SETTINGS_4')]            = (0x74, 0xFF, MAP_BOTH)
field_map[('IQS624', 'HALL_SETTINGS_5')]            = (0x75, 0xFF, MAP_BOTH)
field_map[('IQS624', 'HALL_SETTINGS_6')]            = (0x76, 0xFF, MAP_BOTH)
field_map[('IQS624', 'HALL_SETTINGS_7')]            = (0x77, 0xFF, MAP_BOTH)
field_map[('IQS624', 'HALL_SETTINGS_8')]            = (0x78, 0xFF, MAP_BOTH)
field_map[('IQS624', 'HALL_SETTINGS_9')]            = (0x79, 0xFF, MAP_BOTH)
field_map[('IQS624', 'HALL_SETTINGS_10')]           = (0x7A, 0xFF, MAP_BOTH)
field_map[('IQS624', 'HALL_SETTINGS_11')]           = (0x7B, 0xFF, MAP_BOTH)
field_map[('IQS624', 'HALL_SETTINGS_12')]           = (0x7C, 0xFF, MAP_BOTH)
field_map[('IQS624', 'HALL_SETTINGS_13')]           = (0x7D, 0xFF, MAP_BOTH)
field_map[('IQS624', 'HALL_SETTINGS_14')]           = (0x7E, 0xFF, MAP_BOTH)
field_map[('IQS624', 'HALL_SETTINGS_15')]           = (0x7F, 0xFF, MAP_BOTH)

field_map[('IQS624', 'SYSTEM_SETTINGS')]            = (0xD0, 0x1C, MAP_BOTH)
field_map[('IQS624', 'ACTIVE_CHS')]                 = (0xD1, 0xFF, MAP_BOTH)
field_map[('IQS624', 'PMU_SETTINGS')]               = (0xD2, 0x00, MAP_BOTH)
field_map[('IQS624', 'REPORT_RATES_TIMINGS_0')]     = (0xD3, 0xFF, MAP_BOTH)
field_map[('IQS624', 'REPORT_RATES_TIMINGS_1')]     = (0xD4, 0xFF, MAP_BOTH)
field_map[('IQS624', 'REPORT_RATES_TIMINGS_2')]     = (0xD5, 0xFF, MAP_BOTH)
field_map[('IQS624', 'REPORT_RATES_TIMINGS_3')]     = (0xD6, 0xFF, MAP_BOTH)

field_map[('IQS624', 'RDY_TIMEOUT_PERIOD')]         = (0xD8, 0x00, MAP_BOTH)
field_map[('IQS624', 'I2C_SETTINGS')]               = (0xD9, 0x00, MAP_BOTH)

# IQS625 ---------------------------------------------------------------------

field_map[('IQS625', 'CH0PROXSETTINGS0')]           = (0x40, 0xFF, MAP_BOTH)
field_map[('IQS625', 'CH1PROXSETTINGS0')]           = (0x41, 0xFF, MAP_BOTH)
field_map[('IQS625', 'CH0_1PROXSETTINGS1')]         = (0x42, 0xFF, MAP_BOTH)
field_map[('IQS625', 'CH0PROXSETTINGS2')]           = (0x43, 0xFF, MAP_BOTH)
field_map[('IQS625', 'CH1PROXSETTINGS2')]           = (0x44, 0xFF, MAP_BOTH)
field_map[('IQS625', 'CH0_1PROXSETTINGS3')]         = (0x45, 0xFF, MAP_BOTH)
field_map[('IQS625', 'COMPENSATIONCH0')]            = (0x46, 0xFF, MAP_BOTH)
field_map[('IQS625', 'COMPENSATIONCH1')]            = (0x47, 0xFF, MAP_BOTH)
field_map[('IQS625', 'MULTIPLIERSCH0')]             = (0x48, 0xFF, MAP_BOTH)
field_map[('IQS625', 'MULTIPLIERSCH1')]             = (0x49, 0xFF, MAP_BOTH)

field_map[('IQS625', 'CH0PROXTHR')]                 = (0x50, 0xFF, MAP_BOTH)
field_map[('IQS625', 'CH0TOUCHTHR')]                = (0x51, 0xFF, MAP_BOTH)
field_map[('IQS625', 'CH1PROXTHR')]                 = (0x52, 0xFF, MAP_BOTH)
field_map[('IQS625', 'CH1TOUCHTHR')]                = (0x53, 0xFF, MAP_BOTH)
field_map[('IQS625', 'UIHALTPERIOD')]               = (0x54, 0xFF, MAP_BOTH)

field_map[('IQS625', 'HALLROTUISETTINGS')]          = (0x70, 0x00, MAP_BOTH)
field_map[('IQS625', 'HALLSENSORSETTINGS')]         = (0x71, 0xFF, MAP_BOTH)
field_map[('IQS625', 'CH2_3HALLATISETTINGS')]       = (0x72, 0x00, MAP_BOTH)
field_map[('IQS625', 'CH4_5HALLATISETTINGS')]       = (0x73, 0x00, MAP_BOTH)
field_map[('IQS625', 'COMPENSATIONCH2_3')]          = (0x74, 0xFF, MAP_BOTH)
field_map[('IQS625', 'COMPENSATIONCH4_5')]          = (0x75, 0xFF, MAP_BOTH)
field_map[('IQS625', 'MULTIPLIERSCH2_3')]           = (0x76, 0xFF, MAP_BOTH)
field_map[('IQS625', 'MULTIPLIERSCH4_5')]           = (0x77, 0xFF, MAP_BOTH)
field_map[('IQS625', 'HALLRATIOSETTINGS')]          = (0x78, 0xFF, MAP_BOTH)
field_map[('IQS625', 'SINCONSTANT')]                = (0x79, 0xFF, MAP_BOTH)
field_map[('IQS625', 'COSCONSTANT')]                = (0x7A, 0xFF, MAP_BOTH)
field_map[('IQS625', 'WHEELFILTERBETA')]            = (0x7B, 0xFF, MAP_BOTH)
field_map[('IQS625', 'WHEELWAKEPRELOAD')]           = (0x7C, 0xFF, MAP_BOTH)
field_map[('IQS625', 'INTERVALUIDIVIDER')]          = (0x7D, 0xFF, MAP_BOTH)
field_map[('IQS625', 'WHEELOFFSETL')]               = (0x7E, 0xFF, MAP_BOTH)
field_map[('IQS625', 'WHEELOFFSETH')]               = (0x7F, 0xFF, MAP_BOTH)

field_map[('IQS625', 'GENERALSYSTEMSETTINGS')]      = (0xD0, 0x1C, MAP_BOTH)
field_map[('IQS625', 'ACTIVECHANNELSMASK')]         = (0xD1, 0xFF, MAP_BOTH)
field_map[('IQS625', 'POWERMODESETTINGS')]          = (0xD2, 0x00, MAP_BOTH)
field_map[('IQS625', 'NPREPORTRATE')]               = (0xD3, 0xFF, MAP_BOTH)
field_map[('IQS625', 'LPREPORTRATE')]               = (0xD4, 0xFF, MAP_BOTH)
field_map[('IQS625', 'ULPREPORTRATE')]              = (0xD5, 0xFF, MAP_BOTH)
field_map[('IQS625', 'AUTOMODETIME')]               = (0xD6, 0xFF, MAP_BOTH)

field_map[('IQS625', 'RDYTIMEOUTPERIOD')]           = (0xD8, 0x00, MAP_BOTH)
field_map[('IQS625', 'I2CSETTINGS')]                = (0xD9, 0x00, MAP_BOTH)

# ----------------------------------------------------------------------------

TYPE_INFO = 0
TYPE_PROD = 1
TYPE_HALL = 2
TYPE_MASK = 3
TYPE_DATA = 4

device = ''
device_map = {
    'IQS620A': 0x41,
    'IQS621': 0x46,
    'IQS622': 0x42,
    'IQS624': 0x43,
    'IQS625': 0x4E
}

sar1_map = {
    'IQS620A': (0x50, 0x80),
    'IQS622': (0x48, 0x80)
}

timestamp = datetime.datetime.now()
record_info = '|iqs62x-h2bin|1.0.0|' + timestamp.strftime('%D|')

record = [TYPE_INFO, 0, len(record_info)]
for i in record_info:
    record.append(ord(i))

record_list = [record]
record_pending = False

reg_del = []
reg_map = {}

export_file = open(sys.argv[1], 'r')
export_file_lines = export_file.readlines()

for i in export_file_lines:
    if '*' in i and not device:
        for j in device_map:
            if j in i:
                device = j
                record_list.append([TYPE_PROD, 0, 1, device_map[j]])

        continue

    elif '#define' in i and '0x' in i:
        field_name = i[len('#define'):i.index('0x')].strip()

        if (device, field_name) in field_map:
            (addr, mask, ui_map) = field_map[(device, field_name)]
            data = int(i[i.index('0x'):], 16)

            if mask:
                reg_map[addr] = (data, mask, ui_map)

        continue

    elif 'CH2_3_HALL_ATI_SETTINGS' in i:
        record = [TYPE_HALL, 0x72]

    elif 'CH4_5_HALL_ATI_SETTINGS' in i:
        record = [TYPE_HALL, 0x73]

    else:
        continue

    cal_values = i[(i.index('{') + 1):i.index('}')].split(',')
    record.append(len(cal_values))

    for j in cal_values:
        record.append(int(j, 16))

    record_list.append(record)

export_file.close()

if device in sar1_map:
    (sar1_reg, sar1_mask) = sar1_map[device]
    (data, mask, ui_map) = reg_map[sar1_reg]
    ui_del = MAP_PROX if data & sar1_mask else MAP_SAR1
else:
    ui_del = MAP_NONE

for addr in reg_map:
    (data, mask, ui_map) = reg_map[addr]

    if ui_map == ui_del:
        reg_del.append(addr)

    elif mask != 0xFF:
        record_list.append([TYPE_MASK, addr, 2, mask, data])
        reg_del.append(addr)

for addr in reg_del:
    del reg_map[addr]

for addr in range(max(reg_map) + 2):
    if record_pending and addr in reg_map:
        record.append(reg_map[addr][0])
        record[2] += 1

    elif record_pending and not addr in reg_map:
        record_list.append(record)
        record_pending = False

    elif not record_pending and addr in reg_map:
        record = [TYPE_DATA, addr, 1, reg_map[addr][0]]
        record_pending = True

if not len(record_list):
    print('Empty record list!')
    exit(1)

fw_name = sys.argv[2] if len(sys.argv) > 2 else device.lower() + '.bin'
fw_file = open(fw_name, 'wb')

for i in record_list:
    fw_file.write(bytearray(i))

print('Wrote ' + str(len(record_list)) + ' record(s) to ' + fw_name)

fw_file.close()
