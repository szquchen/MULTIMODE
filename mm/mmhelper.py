import sys
from tkinter import *

class MMHelper():

    def __init__(self, root):

        """List of default values"""
        self.TITLE = 'water example'
        self.NATOM = 4
        self.NSTAT = -1
        self.CONV = '1.D-2'
        self.ICOUPL = 4
        self.ICOUPC = 3
        self.ISCFCI = 3000
        self.IWHICH = 1
        self.IDISC = 0
        self.NROTTR = 0
        self.JMAX = 0
        self.MCHECK = 1
        self.INORM = 1
        self.ICI=-1
        self.NMAX=-4
        self.CUT = '5.0D+3'
        self.EVLJ0 = 0.0
        self.NVALR = 20
        self.KSTEP =0
        self.IPRINT = -3
        self.MATSIZ = 0
        self.IREACT = 0
        self.MOLPRO = 0
        self.MOLINC = 0
        self.XTANPM = None
        self.XMODQ = 1.0
        self.NCONT = 1
        self.NVAL1 = 0
        self.NVAL2 = 0
        self.ICONT = -3
        self.JCONT = '1 2 3 4 5 6  4 4'
        self.MAXSUM = [8, 8, 8, 8]
        self.MAXBAS = [[8,8,8,8,8,8], [8,8,8,8,8,8], [8,8,8,8,8,8], [8,8,8,8,8,8]]
        self.MODINT = 1
        self.MEFF = 0
        self.NCYCLE=0
        self.TOLLAN = '1.D-2'
        self.LANMAX = 2000
        self.LGIV = 1
        self.LAN20 = 500
        self.LANCUT = 0
        self.TOLCUT = '0.D0'
        self.LANCYC = 200
        self.TOLMAT = '1.D-10'
        self.LANINC = 4
        self.NRSYM = 1
        self.NWSYM = 1
        self.ISYMPG = 0
        self.NSYM = 3
        self.ISYM = [1,2,3,4,5,6]
        self.MVSYM = 1
        self.MWSYM = 1
        self.MXDIP = [1,1,1]
        self.MX = [1,2,3]
        self.MXROT = [1,1,1]
        self.ISYMT = 1
        self.LDUMP = 0
        self.MDUMP = 0
        self.IDUMP = [0, 0]
        self.NBF = [12,12,12,12,12,12]
        self.MBF = [16,16,16,16,16,16]
        self.NVF = [8,8,8,8,8,8]
        self.MVF = [12,12,12,12,12,12]
        self.SYMB = ['H','H','C','O']
        self.SSD = None
        self.NPOT = None
        self.IPOT = None
        self.JPOT = None
        self.CPOT = None
        self.NMASS = [12.0, 15.9949, 1.007825, 1.007825]
        self.COORD = """0.143065634079D+01  0.984836585032D+00  0.000000000000D+00
          -0.614302129101D-07 -0.124107359988D+00  0.000000000000D+00
          -0.143065634079D+01  0.984836585032D+00  0.000000000000D+00"""
        self.NCD = None
        self.MAXCHK = [0, 0, 0, 0]
        self.OVF = 'MM.vib'
        self.ORF = 'MM.rot'
        self.LINEAR = 0
        self.NMODE = 3 * self.NATOM - 6 + self.NROTTR
        self.remember = 0
        self.build_window()
        
    def infobox(self, event=None,info=''):
        import sys
        if sys.version_info[0] == 2:
            import Tkinter
            import tkMessageBox

            tkMessageBox.showinfo(*info)
        else:
            from tkinter import messagebox
            messagebox.showinfo(*info)

    def longframe(self, text,default_value = '',info=['Quick Info','Sorry, no info, please see manual.']):
        fm = Frame(root)
        fm.pack()
        label = Label(fm, text=text)
        label.pack(side=LEFT)
        entry = Entry(fm,width=30)
        entry.pack(side=LEFT)
        entry.insert(0, default_value)

        label.bind('<Button-1>', lambda event: self.infobox(event,info))
        return entry

    def shortframe(self, text,default_value = '',info=['Quick Info','Sorry, no info, please see manual.']):
        fm = Frame(root)
        fm.pack()
        label = Label(fm, text=text)
        label.pack(side=LEFT)
        entry = Entry(fm,width=10)
        entry.pack(side=LEFT)
        entry.insert(0, default_value)

        label.bind('<Button-1>', lambda event: self.infobox(event,info))
        return entry

    def build_window(self):                                                     
        bottomFrame = Frame(root)
        bottomFrame.pack(side=BOTTOM)

        Label(root,text="MULTIMODE's Little Helper ",font=("Helvetica", 25)).pack()
        Label(root,text="for MM5.1.4  --ver. 0.01 \n").pack()
        Label(root,text='(Click keywords before entry for quick explanation)').pack()
        Label(root, text="1. Molecule System Information", bg="red", fg="white",font=("Helvetica", 16)).pack()

        self.TITLE_entry = self.longframe('Name of project: ', "H2CO_example", ['Info',
            'The project name used inside `fort.1` file, not the filename.'])
        self.NATOM_entry = self.longframe('Number of atoms: ', 4)
        self.SYMB_entry = self.longframe('Nuclear Symbols: ', 'C O H H', ['Info',
            'Tips: \n1. Separate with spaces.\n2. Order should be consistent with your potential'])
        self.NMASS_entry = self.longframe('Nuclear Masses: ', self.NMASS, ['Info',
            'Mass of carbon is 12.0'])

        Label(root, text='Equilibrium Cartesian Coordinates (in Bohr): ').pack()
        
        text_frame = Frame(root, highlightbackground="green", highlightcolor="green",
            highlightthickness=1, width=100, height=100, bd= 0)
        text_frame.pack()
        self.COORD_text = Text(text_frame, height=5, width=40)
        self.COORD_text.pack(side=TOP)
        self.COORD_text.insert(END, "   0.00000000   0.00000000  -1.14627040\n   0.00000000   0.00000000   1.14354081\n   1.76538873   0.00000000  -2.25018868\n  -1.76538873   0.00000000  -2.25018868")

        Label(root, text="2. VSCF/VCI configurations", bg="red", fg="white",font=("Helvetica", 16)).pack()

        self.ICOUPL_entry = self.shortframe('n-mode representation (ICOUPL): ', 3, ['Info', "n-mode representation of the potential\nCannot exceed the number of normal modes\nTypically 3 or 4"])
        self.NMAX_entry = self.shortframe('Mode-coupling in VCI (|NMAX|): ', 3, ['Info',
            'The number of modes allowed to be excited simultaneously in VCI'])
        self.MAXSUM_entry = self.shortframe('MAXSUM', 8, ['Info',
            'The max sum of excitation in VCI basis'])
        self.MAXBAS_entry = self.shortframe('MAXBAS', 8, ['Info',
            'The max basis function for a single mode'])
        self.NROTTR_entry = self.shortframe('NROTTR', 0, ['Info',
            "0: Use all normal modes\n<-1: Reduced-dimensional calculations using NMODE=3*NATOM-6+NROTTR highest-freq modes"])
        save = Button(root,text='Generate `fort.1`')
        save.pack()
        save.bind('<Button-1>', lambda event: self.update(event))

    def update(self, even):

        self.TITLE = self.TITLE_entry.get()
        self.NATOM = int(self.NATOM_entry.get())
        self.SYMB = self.SYMB_entry.get()
        self.NMASS = self.NMASS_entry.get()
        self.COORD = self.COORD_text.get("1.0", "end-1c")
        self.ICOUPL = int(self.ICOUPL_entry.get())
        self.ICOUPC = self.ICOUPL
        if self.ICOUPC > 2:
            self.ICOUPC = self.ICOUPC - 1
        self.NMAX = int(self.NMAX_entry.get())
        if self.NMAX > 0:
            self.NMAX = -self.NMAX
        self.MAXSUM = int(self.MAXSUM_entry.get())
        self.MAXBAS = int(self.MAXBAS_entry.get())
        self.NROTTR = int(self.NROTTR_entry.get())

        self.NMODE = 3 * self.NATOM - 6 + self.NROTTR
        
        # update variables dependent on the values of other inputs:
        self.ICONT = -self.NMODE
        self.JCONT = ''
        for i in range(self.NMODE):
            self.JCONT += str(i+1)+' '
        self.JCONT += '  ' + str(self.ICOUPL) + ' ' + str(self.ICOUPC)
        self.NSYM = self.NMODE
        self.ISYM = list(range(1, self.NMODE+1))
        self.MAXCHK = [0] * abs(self.NMAX)
        
        NBF = list()
        MBF = list()
        NVF = list()
        MVF = list()
        for node in range(self.NMODE):
            NBF.append(self.MAXBAS+4)
            MBF.append(self.MAXBAS+8)
            NVF.append(self.MAXBAS)
            MVF.append(self.MAXBAS+4)
        self.NBF = NBF
        self.MBF = MBF
        self.NVF = NVF
        self.MVF = MVF

        MAXBAS = list()
        MAXSUM = list()

        for mode in range(abs(self.NMAX)):
            MAXSUM.append(int(self.MAXSUM))
            MAXBAS_temp = list()
            for node in range(self.NMODE):
                MAXBAS_temp.append(int(self.MAXBAS)-mode)
            MAXBAS.append(MAXBAS_temp)

        self.MAXSUM = MAXSUM
        self.MAXBAS = MAXBAS
        self.SYMB = self.SYMB_entry.get().split()
        
        inputs = list()
        inputs.append(self.TITLE)
        inputs.append([self.NATOM, self.NSTAT, self.CONV, self.ICOUPL, self.ICOUPC, self.ISCFCI, self.IWHICH, self.IDISC, self.NROTTR, self.JMAX, self.MCHECK, self.INORM])
        inputs.append([self.ICI, self.NMAX, self.CUT, self.EVLJ0,self.NVALR, self.KSTEP, self.IPRINT, self.MATSIZ, self.IREACT, self.MOLPRO, self.MOLINC])
        inputs.append(self.XTANPM)
        inputs.append(self.XMODQ)
        inputs.append([self.NCONT, self.NVAL1, self.NVAL2])
        inputs.append([self.ICONT, self.JCONT])
        inputs.append(self.MAXSUM)
        inputs.append(self.MAXBAS)
        inputs.append(self.MODINT)
        inputs.append(self.MEFF)
        inputs.append([self.NCYCLE, self.TOLLAN, self.LANMAX, self.LGIV, self.LAN20, self.LANCUT, self.TOLCUT, self.LANCYC, self.TOLMAT, self.LANINC])
        inputs.append([self.NRSYM, self.NWSYM, self.ISYMPG])
        inputs.append([self.NSYM, self.ISYM])
        inputs.append([self.MVSYM, self.MWSYM])
        inputs.append(self.MXDIP)
        inputs.append(self.MX)
        inputs.append(self.MXROT)
        inputs.append(self.ISYMT)
        inputs.append([self.LDUMP, self.MDUMP, self.IDUMP])
        inputs.append([self.NBF, self.MBF, self.NVF, self.MVF])
        inputs.append(self.SYMB)
        inputs.append(self.SSD)
        inputs.append(self.NPOT)
        inputs.append([self.IPOT, self.JPOT, self.CPOT])
        inputs.append(self.NMASS)
        inputs.append(self.COORD)
        inputs.append(self.NCD)
        inputs.append(self.MAXCHK)
        inputs.append(self.OVF)
        inputs.append(self.ORF)
        
        self.generate_fort1(inputs)
        info = ['Info', 'Congratulations, `fort.1` is generated successfully.']
        self.infobox( event=None, info=info)
        #tkinter.messagebox.showinfo()

    def generate_fort1(self,p):
        """

        :param p: An nested array of parameters. p[i] is the (i-1)th line of parameters in orginal `fort.1` input.
        :return: None

        TO-DO:
        1. Input error control
        """
        "Conversion Table"
        TITLE = p[0]
        [NATOM, NSTAT, CONV, ICOUPL, ICOUPC, ISCFCI, IWHICH, IDISC, NROTTR, JMAX, MCHECK, INORM] = p[1]
        [ICI, NMAX, CUT, EVLJ0, NVALR, KSTEP, IPRINT, MATSIZ, IREACT, MOLPRO, MOLINC] = p[2]
        XTANPM = p[3]
        XMODQ = p[4]
        [NCONT, NVAL1, NVAL2] = p[5]
        [ICONT, JCONT] = p[6]
        MAXSUM = p[7]
        MAXBAS = p[8]
        MODINT = p[9]
        MEFF = p[10]
        [NSYM, ISYM] = p[13]
        MXDIP = p[15]
        MX = p[16]
        MXROT = p[17]
        [LDUMP, MDUMP, IDUMP] = p[19]
        [NBF, MBF, NVF, MVF] = p[20]
        NMASS = p[25]
        COORD = p[26]
        MAXCHK = p[28]
        OVF = p[29]
        ORF = p[30]

        "Generating fort.1 file"

        f = open('fort.1', 'w')
        f.write('C**TITLE \n')
        f.write('{:s}\n'.format(p[0]))
        f.write('C**NATOM,NSTAT,CONV,ICOUPL,ICOUPC,ISCFCI,IWHICH,IDISC,NROTTR,JMAX,MCHECK,INORM \n')
        f.write('   {:^6d}{:^5d}{:^5s}{:^7d}{:^7d}{:^7d}{:^7d}{:^6d}{:^8d}{:^5d}{:^7d}{:^5d}\n'.format(*p[1]))
        f.write('C**ICI NMAX  CUT     EVLJ0   NVALR KSTEP IPRINT MATSIZ IREACT MOLPRO MOLINC \n')
        f.write('  {:^5d}{:<6d}{:<8s}{:^5.2f}{:^8d}{:^7d}{:^7d}{:^7d}{:^7d}{:^8d}{:^6d}\n'.format(*p[2]))
        f.write('C**XTANPM (DATA IGNORED IF MOLPRO.EQ.0 AND IWHICH.GE.0)\n')
        f.write('C**XMODQ \n')
        f.write('  ' + ('  ' + str(p[4]))*self.NMODE + '\n')
        f.write('C**NCONT NVAL1 NVAL2 (DATA IGNORED IF NMAX.GE.0 OR ISCFCI.LE.0) \n')
        f.write('   {:^5d} {:^5d} {:^5d} \n'.format(*p[5]))
        f.write('C**ICONT JCONT (DATA IGNORED IF NMAX.GE.0 OR ISCFCI.LE.0) \n')
        f.write('   {:<5d} {:<30s} \n'.format(*p[6]))  # Here JCONT used string
        f.write('C**MAXSUM (DATA IGNORED IF NMAX.GE.0 OR ISCFCI.LE.0) \n')
        if NMAX >= 0 or ISCFCI <= 0:
            pass
        else:
            f.write(('{:4d}' * len(MAXSUM) + '\n').format(*MAXSUM))
        f.write('C**MAXBAS (DATA IGNORED IF NMAX.GE.0 OR ISCFCI.LE.0) \n')
        if NMAX >= 0 or ISCFCI <= 0:
            pass
        else:
            for nbasis in MAXBAS:  # Iterate MAXBAS
                f.write(('{:4d}' * len(nbasis) + '\n').format(*nbasis))
        f.write('C**MODINT\n')
        f.write('  ' + ('  ' + str(self.MODINT))*self.NMODE + '\n')
        f.write('C**MEFF\n')
        f.write('  ' + ('  ' + str(self.MEFF))*self.NMODE + '\n')
        f.write('  ' + ('  ' + str(self.MEFF))*self.NMODE + '\n')
        f.write('C**NCYCLE,TOLLAN,LANMAX,LGIV,LAN20,LANCUT,TOLCUT,LANCYC,TOLMAT, LANINC (LANCZOS)\n')
        f.write('   {:^7d}{:^7s}{:^7d}{:^5d}{:^5d}{:^7d}{:^7s}{:^7d}{:^8s}{:^8d}\n'.format(*p[11]))
        f.write('C**NRSYM NWSYM ISYMPG\n')
        f.write('  {:^6d}{:^6d}{:^6d}\n'.format(*p[12]))
        f.write('C**NSYM ISYM (ORDER A1,B2,B1,A2) \n')
        f.write(('  {:^6d}' + '{:3d}' * len(ISYM) + '\n').format(NSYM, *ISYM))
        f.write('C**MVSYM   MWSYM \n')
        f.write('   {:^5d}   {:^5d}\n'.format(*p[14]))
        f.write('C**MXDIP (I.R. of mu(X), mu(Y), mu(Z))\n')
        f.write(('{:5d}' * len(MXDIP) + '\n').format(*MXDIP))
        f.write('C**MX (symmetry axes x,y,z corresponding to principle axes X,Y,Z)\n')
        f.write(('{:5d}' * len(MX) + '\n').format(*MX))
        f.write('C**MXROT (I.R. of Rx, Ry, Rz) \n')
        f.write(('{:5d}' * len(MXROT) + '\n').format(*MXROT))
        f.write('C**ISYMT (I.R. of Sin(M.tau/2)\n')
        f.write('{:5d}\n'.format(p[18]))
        f.write('C**LDUMP MDUMP IDUMP (DATA IGNORED IF ICI.GE.0)\n')
        if ICI >= 0:
            pass
        else:
            f.write((('  ' + '{:^5d}' * 2 + '  ' + '{:>3d}' * len(IDUMP) + '\n').format(LDUMP, MDUMP, *IDUMP)))
        f.write('C**NBF,MBF,NVF,MVF \n')
        for i in range(len(NBF)):
            f.write(('{:5d}' * 4 + '\n').format(NBF[i], MBF[i], NVF[i], MVF[i]))
        f.write('C**NUCLEAR SYMBOLS\n')
        f.write((' {:2s}' * NATOM + '\n').format(*p[21]))
        f.write('C**SCF STATE DEFINITIONS (SEE ORIGINAL DEFINITION BY JELSKI) \n')
        f.write('C**NPOT (IGNORED IF IWHICH!=0) \n')
        f.write('C**IPOT,JPOT,CPOT (ONLY IF INORM=0)\n')
        if self.INORM == 0:
            for i in range(self.NMODE):
                f.write(('{:2d}' + ' 0 0 0 0 0  2 0 0 0 0 0\n').format(i+1))
        f.write('C**NUCLEAR MASSES (XM(I),I=1,NATOM)\n')
        f.write(('{:s}' + '\n').format(self.NMASS))
        f.write('C**EQUILIBRIUM CARTESIAN COORDINATES ((X0(I,J),J=x,y,z),I=1,NATOM)\n')
        f.write(COORD)
        f.write('\n')
        f.write('C**NORMAL COORDINATE DISPLACEMENTS (((XL(I,J,K),K=x,y,z),I=1,NATOM),J=1,NMODE)\n')
        f.write('C**MAXCHK \n')
        f.write(('{:4d}' * len(MAXCHK) + '\n').format(*MAXCHK))
        f.write('C**OUTPUT VIBRATION FILE\n')
        f.write('{:<30s}\n'.format(p[29]))
        f.write('C**OUTPUT ROTATION FILE\n')
        f.write('{:<30s}'.format(p[30]))

        f.close
        return

if __name__ == '__main__':
    root = Tk()
    app = MMHelper(root)
    root.mainloop()
