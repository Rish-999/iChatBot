# backend/services/chat_service.py

# ---------------- Chat Flow ----------------
chat_flow = {
    # ---------------- Start ----------------
    "start": {
        "message": "Hello! What do you want help with?",
        "options": ["Tech Support", "Service Support", "Order Status"]
    },

    # ---------------- Tech Support ----------------
    "Tech Support": {
        "message": "Please choose your issue category.",
        "options": ["Machine Error", "Troubleshooting", "Back to Start"]
    },

    # Troubleshooting Branch
    "Troubleshooting": {
        "message": "Select the issue you are facing.",
        "options": [
            "Hopper Error – Troubleshooting",
            "Span Error – Troubleshooting",
            "Board Malfunction",
            "Fuse Blown (PS-2 Unit)",
            "Weigh/Drive Unit Malfunction",
            "Zero Error – Troubleshooting",
            "Back to Tech Support", "Back to Start"
        ]
    },

    "Hopper Error – Troubleshooting": {
        "message": (
            "⚠️ Hopper Error – Troubleshooting:\n"
             "Causes & Fixes:\n"
            "- Product stuck in hopper gates → Remove products & check gate movement\n"
            "- Loose screw on cam sensor → Repair weigh/drive unit\n"
            "- Board malfunction → Replace cam sensor board (P-5207*)\n"
            "- Connector short/failure → Check DUC board (P-5524*) connectors\n"
            "- Fuse blown (PS-2 unit) → Replace mini fuses (P-5508* / PS-2 unit, 125V SA)\n"
            "- DUC board malfunction → Replace DUC board (P-5524*)\n"
            "- Weigh/drive unit malfunction → Repair or replace unit"
        ),
        "options": ["Back to Troubleshooting", "Back to Start"]
    },

    "Span Error – Troubleshooting": {
        "message": (
            "⚖️ Span Error – Troubleshooting:\n"
             "Causes & Fixes:\n"
            "- ADC board malfunction → Replace ADC board (P-5576*)\n"
            "- Incorrect calibration → Use 200g span adjustment weight"
        ),
        "options": ["Back to Troubleshooting", "Back to Start"]
    },

    "Board Malfunction": {
        "message": (
            "🔌 Board Malfunction:\n"
            "- Replace faulty board (check part number)\n"
            "- Verify connectors are secure\n"
            "- If issue persists → escalate to service team"
        ),
        "options": ["Back to Troubleshooting", "Back to Start"]
    },

    "Fuse Blown (PS-2 Unit)": {
        "message": (
            "💡 Fuse Blown (PS-2 Unit):\n"
            "- Replace mini fuses on DC fuse boards (P-5508*) & PS-2 unit (125V SA)\n"
            "- Ensure no short circuit before replacement"
        ),
        "options": ["Back to Troubleshooting", "Back to Start"]
    },

    "Weigh/Drive Unit Malfunction": {
        "message": (
            "⚙️ Weigh/Drive Unit Malfunction:\n"
            "- Inspect & repair weigh/drive unit\n"
            "- If damage is severe → replace the unit"
        ),
        "options": ["Back to Troubleshooting", "Back to Start"]
    },

    "Zero Error – Troubleshooting": {
        "message": (
            "⚠️ Zero Error – Troubleshooting:\n"
            "- DUC board (P-5524*) malfunction → Replace\n"
            "- ADC board (P-5576*) malfunction → Replace\n"
            "- Preamp board (P-5527*, dispersion feeder only) → Replace\n"
            "- Load cell issue → Replace load cell\n"
            "- ±15V power malfunction → Check J324 (ADC board), replace PS-CAL unit"
        ),
        "options": ["Back to Troubleshooting", "Back to Start"]
    },

    # ---------------- Machine Error ----------------
    "Machine Error": {
        "message": "Do you see an error displayed on the screen?",
        "options": ["With Error Display", "Without Error Display", "Back to Tech Support", "Back to Start"]
    },

    "With Error Display": {
        "message": "Select the error status:",
        "options": [
            "Zero Error – With Display",
            "Hopper Error – With Display",
            "125V SA",
            "Back to Machine Error",
            "Back to Start"
        ]
    },

    "Zero Error – With Display": {
        "message": (
            "Zero Error (With Display):\n\n"
            "1. Board malfunction → Replace DUC board (P-5524*).\n"
            "2. ADC failure → Replace ADC board (P-5576*).\n"
            "3. Preamp board failure (dispersion feeder only) → Replace preamp board (P-5527*).\n"
            "4. Weigh mechanism malfunction → Replace load cell.\n"
            "5. ±15V power malfunction → Check ADC board J324 connector or replace PS-CAL unit."
        ),
        "options": ["Back to With Error Display", "Back to Machine Error", "Back to Start"]
    },

    "Hopper Error – With Display": {
        "message": (
            "Hopper Error (With Display):\n\n"
            "1. Product caught in hopper gates → Remove product and check smooth movement.\n"
            "2. Loose screw on cam sensor inside weigh/drive unit → Repair weigh/drive unit.\n"
            "3. Board malfunction → Replace cam sensor board (P-5207*).\n"
            "4. Short circuit/contact failure → Check continuity of DUC board connectors.\n"
            "5. Fuse blown (PS-2 unit) → Replace mini fuses on DC fuse boards (P-5508*) and PS-2 unit."
        ),
        "image": "/static/Screenshot 2025-09-09 155746.png",
        "options": ["Back to With Error Display", "Back to Machine Error", "Back to Start"]
    },

    "125V SA": {
        "message": (
            "125V SA Error:\n\n"
            "1. Board malfunction → Replace DUC board (P-5524*).\n"
            "2. Weigh/drive unit malfunction → Repair or replace the weigh/drive unit."
        ),
        "options": ["Back to With Error Display", "Back to Machine Error", "Back to Start"]
    },

    "Without Error Display": {
        "message": "Select the issue you are facing:",
        "options": [
            "Nothing Displayed",
            "Weigher Does Not Operate",
            "Back to Machine Error",
            "Back to Start"
        ]
    },

    "Nothing Displayed": {
        "message": (
            "Nothing Displayed on Remote Unit:\n"
             "Causes & Fixes:\n"
            "1. Main power switch is OFF → Turn on.\n"
            "2. Power switch/breaker is OFF → Turn on (PS-0 unit).\n"
            "3. Open circuit/contact failure → Check XT602 (PS-0) and XC50 connector.\n"
            "4. Chattering when power on → Restart power.\n"
            "5. Display malfunction → Replace Fluorescent Display unit."
        ),
        "options": ["Back to Without Error Display", "Back to Machine Error", "Back to Start"]
    },

    "Weigher Does Not Operate": {
        "message": (
            "Weigher Does Not Operate (Power ON but not working):\n\n"
             "Causes & Fixes:\n"
            "1. DUC board malfunction → Replace DUC board (P-5524*).\n"
            "2. Component malfunction → Replace KM01 (electromagnetic contactor).\n"
            "3. Open circuit/contact failure → Check XT601 (PS-0), XJ453 (Relay board P-5526*), J303 (WCU board P-5561*).\n"
            "4. Interlock signal not input (LED not flashing) → Run packaging machine or check interlock cables (DC24V).\n"
            "5. Interlock abnormal (LED flashing) → Replace relay board (P-5526*) or check connection to WCU board J305.\n"
            "6. FDC board malfunction → Replace FDC board (P-5423*)."
        ),
        "options": ["Back to Without Error Display", "Back to Machine Error", "Back to Start"]
    },

    # ---------------- Service Support ----------------
    "Service Support": {
        "message": "Welcome to Service Support. How can we assist you today?",
        "options": [
            "Request Technician Visit",
            "Spare Parts & Repairs",
            "Preventive Maintenance",
            "Annual Maintenance Contract (AMC)",
            "Escalation / Contact Service Team",
            "Back to Start"
        ]
    },

    "Request Technician Visit": {
        "message": (
            "🛠️ Requesting a Technician Visit:\n\n"
            "- Our certified technician will visit your site to diagnose & fix the machine issue.\n"
            "- Typical response time: 24–48 hours (depending on location).\n"
            "- You may need to provide:\n"
            "   • Machine Serial Number\n"
            "   • Error Code (if displayed)\n"
            "   • Contact Person & Address\n\n"
            "👉 Would you like us to guide you to submit a **Service Request Form**?"
        ),
        "options": ["Back to Service Support", "Back to Start"]
    },

    "Spare Parts & Repairs": {
        "message": (
            "⚙️ Spare Parts & Repairs:\n\n"
            "- Genuine spare parts available for boards, load cells, sensors, and fuses.\n"
            "- Repairs are carried out at our authorized service centers.\n"
            "- You may be asked for:\n"
            "   • Part number / description\n"
            "   • Machine serial number\n"
            "- Warranty check will be performed before replacement.\n\n"
            "👉 Would you like a list of commonly replaced parts?"
        ),
        "options": ["Back to Service Support", "Back to Start"]
    },

    "Preventive Maintenance": {
        "message": (
            "🧹 Preventive Maintenance (PM):\n\n"
            "- Regular maintenance ensures longer machine life and fewer breakdowns.\n"
            "- Includes:\n"
            "   • Cleaning and inspection of hopper gates, boards, load cells\n"
            "   • Calibration checks\n"
            "   • Firmware updates (if applicable)\n"
            "- Recommended frequency: once every 6 months (depending on usage).\n\n"
            "👉 Do you want to schedule a PM visit?"
        ),
        "options": ["Back to Service Support", "Back to Start"]
    },

    "Annual Maintenance Contract (AMC)": {
        "message": (
            "📑 Annual Maintenance Contract (AMC):\n\n"
            "- Covers unlimited breakdown visits + scheduled preventive maintenance.\n"
            "- Includes labor charges (parts may be extra depending on AMC type).\n"
            "- Priority service compared to non-AMC customers.\n"
            "- Types:\n"
            "   1. Comprehensive AMC – covers service + parts\n"
            "   2. Non-Comprehensive AMC – covers service only\n\n"
            "👉 Would you like to request an AMC quotation?"
        ),
        "options": ["Back to Service Support", "Back to Start"]
    },

    "Escalation / Contact Service Team": {
        "message": (
            "📞 Escalation / Contact Service Team:\n\n"
            "- If your issue is urgent or unresolved, you can contact:\n"
            "   • Toll-Free Support Number: 1800-123-456\n"
            "   • Email: support@example.com\n"
            "   • WhatsApp Chat: +91-98765-43210\n"
            "- Our service team works Mon–Sat, 9 AM – 6 PM.\n\n"
            "👉 Would you like me to share the **Escalation Matrix** (service manager contacts)?"
        ),
        "options": ["Back to Service Support", "Back to Start"]
    }
}

# ---------------- Service Methods ----------------
def root():
    return {"status": "ok", "message": "FastAPI server is running 🚀"}

def get_start():
    return chat_flow["start"]

def get_response(query: str):
    query = query.strip()

    # Handle back-navigation dynamically
    if query.startswith("Back to "):
        target = query.replace("Back to ", "").strip()
        if target in chat_flow:
            return chat_flow[target]
        return chat_flow["start"]

    # Normal case
    return chat_flow.get(query, {
        "message": f"❓ I don’t understand '{query}'. Please try again.",
        "options": chat_flow["start"]["options"]
    })






# chat_flow = {
#
#     "start": {
#         "message": "Hello! What do you want help with?",
#         "options": ["Tech Support", "Service Support", "Order Status"]
#     },
#     # ---------------- Tech Support ----------------
#     "Tech Support": {
#         "message": "Please choose your issue category.",
#         "options": [ "Machine Error", "Troubleshooting"]
#     },
#
#     "Troubleshooting": {
#         "message": "Select the issue you are facing.",
#         "options": ["Hopper Error", "Span Error", "Board Malfunction", "Fuse Blown (PS-2 Unit)",
#                     "Weigh/Drive Unit Malfunction", "Zero Error"]
#     },
#
#     "Hopper Error": {
#         "message": (
#             "⚠️ Hopper Error – Possible Causes & Fixes:\n"
#             "- Product stuck in hopper gates → Remove products & check gate movement\n"
#             "- Loose screw on cam sensor → Repair weigh/drive unit\n"
#             "- Board malfunction → Replace cam sensor board (P-5207*)\n"
#             "- Connector short/failure → Check DUC board (P-5524*) connectors\n"
#             "- Fuse blown (PS-2 unit) → Replace mini fuses (P-5508* / PS-2 unit, 125V SA)\n"
#             "- DUC board malfunction → Replace DUC board (P-5524*)\n"
#             "- Weigh/drive unit malfunction → Repair or replace unit"
#         ),
#         "options": ["Back to Troubleshooting", "Back to Start"]
#     },
#
#     "Span Error": {
#         "message": (
#             "⚖️ Span Error – Possible Causes & Fixes:\n"
#             "- ADC board malfunction → Replace ADC board (P-5576*)\n"
#             "- Incorrect calibration → Use 200g span adjustment weight"
#         ),
#         "options": ["Back to Troubleshooting", "Back to Start"]
#     },
#
#     "Board Malfunction": {
#         "message": (
#             "🔌 Board Malfunction – Possible Fixes:\n"
#             "- Replace faulty board (check part number)\n"
#             "- Verify connectors are secure\n"
#             "- If issue persists → escalate to service team"
#         ),
#         "options": ["Back to Troubleshooting", "Back to Start"]
#     },
#
#     "Fuse Blown (PS-2 Unit)": {
#         "message": (
#             "💡 Fuse Blown – Possible Fixes:\n"
#             "- Replace mini fuses on DC fuse boards (P-5508*) & PS-2 unit (125V SA)\n"
#             "- Ensure no short circuit before replacement"
#         ),
#         "options": ["Back to Troubleshooting", "Back to Start"]
#     },
#
#     "Weigh/Drive Unit Malfunction": {
#         "message": (
#             "⚙️ Weigh/Drive Unit Malfunction – Possible Fixes:\n"
#             "- Inspect & repair weigh/drive unit\n"
#             "- If damage is severe → replace the unit"
#         ),
#         "options": ["Back to Troubleshooting", "Back to Start"]
#     },
#
#     "Zero Error": {
#         "message": (
#             "⚠️ Zero Error – Causes & Fixes:\n"
#             "- DUC board (P-5524*) malfunction → Replace\n"
#             "- ADC board (P-5576*) malfunction → Replace\n"
#             "- Preamp board (P-5527*, dispersion feeder only) → Replace\n"
#             "- Load cell issue → Replace load cell\n"
#             "- ±15V power malfunction → Check J324 (ADC board), replace PS-CAL unit"
#         ),
#         "options": ["Back to Troubleshooting", "Back to Start"]
#     },
#
#     # ---------------- Machine Errors ----------------
#     "Machine Error": {
#         "message": "Do you see an error displayed on the screen?",
#         "options": ["With Error Display", "Without Error Display", "Back to Tech Support", "Back to Start"]
#     },
#
#     "With Error Display": {
#         "message": "Select the error status:",
#         "options": ["Zero Error (Machine)", "Hopper Error (Machine)", "125V SA", "Back to Machine Error", "Back to Start"]
#     },
#
#     "Zero Error (Machine)": {
#         "message": (
#             "Zero Error (Machine Display):\n\n"
#             "1. Board malfunction → Replace DUC board (P-5524*).\n"
#             "2. ADC failure → Replace ADC board (P-5576*).\n"
#             "3. Preamp board failure (dispersion feeder only) → Replace preamp board (P-5527*).\n"
#             "4. Weigh mechanism malfunction → Replace load cell.\n"
#             "5. ±15V power malfunction → Check ADC board J324 connector or replace PS-CAL unit."
#         ),
#         "options": ["With Error Display", "Back to Machine Error", "Back to Start"]
#     },
#
#     "Hopper Error (Machine)": {
#         "message": (
#             "Hopper Error (Machine Display):\n\n"
#             "1. Product caught in hopper gates → Remove product and check smooth movement.\n"
#             "2. Loose screw on cam sensor inside weigh/drive unit → Repair weigh/drive unit.\n"
#             "3. Board malfunction → Replace cam sensor board (P-5207*).\n"
#             "4. Short circuit/contact failure → Check continuity of DUC board connectors.\n"
#             "5. Fuse blown (PS-2 unit) → Replace mini fuses on DC fuse boards (P-5508*) and PS-2 unit."
#         ),
#         "options": ["With Error Display", "Back to Machine Error", "Back to Start"]
#     },
#
#     "125V SA": {
#         "message": (
#             "125V SA Error:\n\n"
#             "1. Board malfunction → Replace DUC board (P-5524*).\n"
#             "2. Weigh/drive unit malfunction → Repair or replace the weigh/drive unit."
#         ),
#         "options": ["With Error Display", "Back to Machine Error", "Back to Start"]
#     },
#
#     "Without Error Display": {
#         "message": "Select the issue you are facing:",
#         "options": ["Nothing Displayed", "Weigher Does Not Operate", "Back to Machine Error", "Back to Start"]
#     },
#
#     "Nothing Displayed": {
#         "message": (
#             "Nothing Displayed on Remote Unit:\n\n"
#             "1. Main power switch is OFF → Turn on.\n"
#             "2. Power switch/breaker is OFF → Turn on (PS-0 unit).\n"
#             "3. Open circuit/contact failure → Check XT602 (PS-0) and XC50 connector.\n"
#             "4. Chattering when power on → Restart power.\n"
#             "5. Display malfunction → Replace Fluorescent Display unit."
#         ),
#         "options": ["Without Error Display", "Back to Machine Error", "Back to Start"]
#     },
#
#     "Weigher Does Not Operate": {
#         "message": (
#             "Weigher Does Not Operate (Power ON but not working):\n\n"
#             "1. DUC board malfunction → Replace DUC board (P-5524*).\n"
#             "2. Component malfunction → Replace KM01 (electromagnetic contactor).\n"
#             "3. Open circuit/contact failure → Check XT601 (PS-0), XJ453 (Relay board P-5526*), J303 (WCU board P-5561*).\n"
#             "4. Interlock signal not input (LED not flashing) → Run packaging machine or check interlock cables (DC24V).\n"
#             "5. Interlock abnormal (LED flashing) → Replace relay board (P-5526*) or check connection to WCU board J305.\n"
#             "6. FDC board malfunction → Replace FDC board (P-5423*)."
#         ),
#         "options": ["Without Error Display", "Back to Machine Error", "Back to Start"]
#     },
#
#     # ---------------- Checkweigher ----------------
#     "CHW": {
#         "message": "Select the CHW error you are facing:",
#         "options": ["Zero Error (CHW)", "Span Error (CHW)", "Overweight Error", "Back to Start"]
#     },
#
#     "Zero Error (CHW)": {
#         "message": (
#             "ZERO Error (CHW):\n\n"
#             "Causes:\n"
#             "1. Product remains in weigh hopper.\n"
#             "2. Product spilling from pool hopper.\n\n"
#             "Actions:\n"
#             "- Remove products remaining in weigh hoppers.\n"
#             "- Check for loose, broken, or fallen screws in weigh hoppers.\n"
#             "- If not resolved, ADC board or power supply may be faulty – contact service."
#         ),
#         "options": ["CHW", "Back to Start"]
#     },
#
#     "Span Error (CHW)": {
#         "message": (
#             "Span Error (CHW):\n\n"
#             "Cause: Span adjustment exceeds allowable range due to improper weight.\n\n"
#             "Actions:\n"
#             "- Use proper span adjustment weight:\n"
#             "   • Standard capacity: 200g\n"
#             "   • Medium capacity: 400g\n"
#             "   • High capacity: 500g\n"
#             "   • Extra capacity: 1000g\n"
#             "- If still not resolved → ADC board or power supply may be faulty – contact service."
#         ),
#         "options": ["Checkweigher", "Back to Start"]
#     },
#
#     "Overweight Error": {
#         "message": (
#             "OVERWEIGHT Error (CHW):\n\n"
#             "Causes:\n"
#             "1. Excessive product fed into weigh hopper.\n"
#             "2. Excessive product fed onto dispersion table.\n"
#             "3. Upper limit set too low.\n\n"
#             "Actions:\n"
#             "- If 1–3 heads selected, reduce feeder amplitude/time.\n"
#             "- Decrease supply from infeed conveyor or lower infeed control phototube.\n"
#             "- Decrease DF weight of load cell.\n"
#             "- For heavy piece products → increase upper limit."
#         ),
#         "options": ["CHW", "Back to Start"]
#     }
#
# }
#
#
# # now assign back-links dynamically
# chat_flow["Back to Troubleshooting"] = {
#     "message": "Taking you back to Troubleshooting.",
#     "options": chat_flow["Troubleshooting"]["options"]
# }
# chat_flow["Back to Tech Support"] = {
#     "message": "Taking you back to Tech Support.",
#     "options": chat_flow["Tech Support"]["options"]
# }
# chat_flow["Back to Start"] = {
#     "message": "Taking you back to Start.",
#     "options": chat_flow["start"]["options"]
# }
#
# def root():
#     return {"status": "ok", "message": "FastAPI server is running 🚀"}
#
# def get_start():
#     return chat_flow["start"]
#
# def get_response(query: str):
#     query = query.strip()  # clean user input
#     return chat_flow.get(query, {
#         "message": f"❓ I don’t understand '{query}'. Please try again.",
#         "options": chat_flow["start"]["options"]  # suggest restart options
#     })
