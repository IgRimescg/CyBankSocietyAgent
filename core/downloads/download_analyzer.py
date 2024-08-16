import re
import sys
import json

try:
    from wh1tem0cha import Wh1teM0cha
except:
    print("Error: >wh1tem0cha< module not found.")



class AppleAnalyzer:
    def __init__(self, target_file):
        self._target_binary_buff = open(target_file, "rb").read()
        self.wmocha_object = None 

    def _check_macho_binary(self, target_file):
        # Check MACH-O pattern using wh1tem0cha
        
        wm = Wh1teM0cha(target_file)
        try:
            wm.get_binary_info()
            self.wmocha_object = wm
            return True
        except:
            return False
        
    def analyze_macho_binary(self):
        # Print binary info first
        print(f"Binary Information")
        binary_info = self.wmocha_object.get_binary_info()
        for key in binary_info:
            print(f"[bold magenta]>>>>[white] {key}: [bold green]{binary_info[key]}")

        # Parse segment information
        print(f"\n Parsing segment information...")
        seg_table = Table()
        seg_table.add_column("[bold green]name", justify="center")
        seg_table.add_column("[bold green]offset", justify="center")
        seg_table.add_column("[bold green]cmd", justify="center")
        seg_table.add_column("[bold green]cmdsize", justify="center")
        seg_table.add_column("[bold green]vmaddr", justify="center")
        seg_table.add_column("[bold green]vmsize", justify="center")
        seg_table.add_column("[bold green]filesize", justify="center")
        segments = self.wmocha_object.get_segments()
        for seg in segments:
            seg_inf = self.wmocha_object.segment_info(seg["segment_name"].decode())
            seg_table.add_row(seg["segment_name"].decode(), seg_inf["offset"], seg_inf["cmd"], seg_inf["cmdsize"],
                              seg_inf["vmaddr"], seg_inf["vmsize"], seg_inf["filesize"])
        print(seg_table)

        # Parsing sections
        print(f"\n Analyzing sections...")
        sec_table = Table()
        sec_table.add_column("[bold green]name", justify="center")
        sec_table.add_column("[bold green]segment", justify="center")
        sec_table.add_column("[bold green]offset", justify="center")
        sec_table.add_column("[bold green]size", justify="center")
        sections = self.wmocha_object.get_sections()
        for sec in sections:
            try:
                sec_inf = self.wmocha_object.section_info(sec["section_name"].decode())
                if "__gosymtab" in sec["section_name"].decode() or "__gopclntab" in sec["section_name"].decode() or "__go_buildinfo" in sec["section_name"].decode():
                    sec_table.add_row(f"[bold red]{sec['section_name'].decode()}[white]", sec_inf["segment_name"].decode(), 
                                      sec_inf["offset"].decode(), sec_inf["size"].decode())
                else:
                    sec_table.add_row(sec["section_name"].decode(), sec_inf["segment_name"].decode(),
                                      sec_inf["offset"].decode(), sec_inf["size"].decode())
            except:
                continue
        print(sec_table)

        # Analyze libraries
        print(f"\n Analyzing libraries...")
        self.parse_libraries()

        # Pattern scanner
        print(f"\n Performing pattern scan...")
        self._perform_pattern_analysis()


    def parse_libraries(self):
        library_dict = self.wmocha_object.get_dylib_names()
        if library_dict:
            ltable = Table()
            ltable.add_column("[bold green]Dynamic Libraries",justify="center")
            for lib in library_dict:
                if "/Security" in lib["libname"].decode() or "/libresolv" in lib["libname"].decode() or "/libSystem" in lib["libname"].decode():
                    ltable.add_row(f"[bold red]{lib['libname'].decode()} (Possible malicious purposes!)[white]")
                else:
                    ltable.add_row(lib["libname"].decode())
            print(ltable)

    def _perform_pattern_analysis(self):
        osx_patterns = json.load(open(f"{sc0pe_path}{path_seperator}Systems{path_seperator}OSX{path_seperator}osx_sym_categories.json"))
        for key in osx_patterns:
            for pattern in osx_patterns[key]["patterns"]:
                if re.findall(pattern.encode(), self._target_binary_buff):
                    osx_patterns[key]["occurence"] += 1
                    dict_categ[key].append(pattern)
        self._categ_parser()
        self._print_statistics()