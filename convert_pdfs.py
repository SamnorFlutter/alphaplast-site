import fitz, os, pathlib

src = pathlib.Path(r"C:\Users\Windows 11\Desktop\Alpha plast")
dst = pathlib.Path(r"C:\Users\Windows 11\alphaplast-redesign\assets")
dst.mkdir(parents=True, exist_ok=True)

mapping = {
    "Благодарность (2).pdf":  "cert-thanks-1.png",
    "Благодарн1 (2).pdf":     "cert-thanks-2.png",
    "Благодарность3 (2).pdf": "cert-thanks-3.png",
    "487699e1-3746-48ec-b7b3-a698695e1342.pdf": "cert-guvohnoma-1.png",
    "c6268146-8d7e-46cf-ba16-975c0e892413.pdf": "cert-guvohnoma-2.png",
}

# Also copy PDFs for download
for pdf_name, png_name in mapping.items():
    p = src / pdf_name
    if not p.exists():
        print("MISSING:", pdf_name); continue
    doc = fitz.open(p)
    page = doc.load_page(0)
    pix = page.get_pixmap(matrix=fitz.Matrix(2.0, 2.0))  # 2x for retina
    out = dst / png_name
    pix.save(out)
    # Also copy PDF
    pdf_out = dst / png_name.replace(".png", ".pdf")
    pdf_out.write_bytes(p.read_bytes())
    print(f"OK: {png_name} ({pix.width}x{pix.height})")
    doc.close()
print("DONE")
