def premium_message(combo, stake):
    msg=f"🔥 {combo['type']}\n\n"
    if 'explanation' in combo:
        for i,e in enumerate(combo['explanation'],1):
            msg+=f"{i}️⃣ {e['match']}\n✔ {e['pick']}\n📊 {e['reason']}\n\n"
    if 'picks' in combo:
        for p in combo['picks']:
            msg+=f"✔ {p[0]} – {p[1]}\n"
    msg+=f"\n💰 Momio: {combo['odds']}\n💵 Apuesta: ${stake}\n🏆 Posible: ${round(stake*combo['odds'],2)}"
    return msg
