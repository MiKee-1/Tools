import sys
from pypdf import PdfWriter


def unisci_pdf(pdf_list, output):
    """Unisce un numero arbitrario di PDF in un unico file di output."""
    merger = PdfWriter()

    for pdf in pdf_list:
        merger.append(pdf)

    with open(output, "wb") as file_output:
        merger.write(file_output)

    merger.close()
    print(f"Uniti {len(pdf_list)} PDF in: {output}")


def seleziona_con_finestra():
    """Apre delle finestre per scegliere i PDF da unire e dove salvarli."""
    import tkinter as tk
    from tkinter import filedialog, messagebox

    root = tk.Tk()
    root.withdraw()  # nasconde la finestra principale

    pdf_list = filedialog.askopenfilenames(
        title="Seleziona i PDF da unire (tieni premuto Ctrl per sceglierne piu di uno)",
        filetypes=[("File PDF", "*.pdf")],
    )

    if not pdf_list:
        messagebox.showinfo("Annullato", "Nessun PDF selezionato.")
        return None, None

    if len(pdf_list) < 2:
        messagebox.showwarning(
            "Pochi file", "Seleziona almeno due PDF da unire."
        )
        return None, None

    output = filedialog.asksaveasfilename(
        title="Salva il PDF unito come...",
        defaultextension=".pdf",
        initialfile="merged.pdf",
        filetypes=[("File PDF", "*.pdf")],
    )

    if not output:
        messagebox.showinfo("Annullato", "Salvataggio annullato.")
        return None, None

    return list(pdf_list), output


if __name__ == "__main__":
    # Uso da riga di comando: python merge_pdf.py out.pdf in1.pdf in2.pdf in3.pdf ...
    if len(sys.argv) > 1:
        output = sys.argv[1]
        pdf_list = sys.argv[2:]
        if len(pdf_list) < 2:
            print("Uso: python merge_pdf.py <output.pdf> <input1.pdf> <input2.pdf> [input3.pdf ...]")
            sys.exit(1)
        unisci_pdf(pdf_list, output)
    else:
        # Nessun argomento: apre la selezione grafica dei file
        pdf_list, output = seleziona_con_finestra()
        if pdf_list and output:
            unisci_pdf(pdf_list, output)
