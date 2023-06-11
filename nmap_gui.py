import nmap
import tkinter as tk

class NmapGUI(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Create the scan options
        self.scan_options = tk.Frame(self)
        self.scan_type = tk.Radiobutton(self.scan_options, text="SYN", value="SYN")
        self.scan_type.pack()
        self.scan_type = tk.Radiobutton(self.scan_options, text="UDP", value="UDP")
        self.scan_type.pack()
        self.scan_type = tk.Radiobutton(self.scan_options, text="TCP", value="TCP")
        self.scan_type.pack()

        # Create the scan targets
        self.scan_targets = tk.Frame(self)
        self.target_ip = tk.Entry(self.scan_targets)
        self.target_ip.pack()
        self.target_port = tk.Entry(self.scan_targets)
        self.target_port.pack()

        # Create the scan button
        self.scan_button = tk.Button(self, text="Scan", command=self.scan)
        self.scan_button.pack()

        # Create the scan results
        self.scan_results = tk.Text(self)
        self.scan_results.pack()

    def scan(self):
        # Get the scan options
        scan_type = self.scan_type.get()
        target_ip = self.target_ip.get()
        target_port = self.target_port.get()

        # Create an nmap scanner
        nmap_scanner = nmap.PortScanner()

        # Run the scan
        nmap_scanner.scan(target_ip, target_port, scan_type)

        # Get the scan results
        scan_results = nmap_scanner.scaninfo()

        # Display the scan results
        self.scan_results.insert(tk.END, scan_results)

if __name__ == "__main__":
    root = tk.Tk()
    nmap_gui = NmapGUI(root)
    root.mainloop()
