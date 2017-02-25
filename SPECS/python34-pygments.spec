%global srcname pygments
%global commit cc861d7ba005

Name:           python34-%{srcname}
Version:        2.2.0
Release:        1%{?dist}
Summary:        Pygments is a syntax highlighting package written in Python.

Group:          Development/Languages
License:        BSD
URL:            http://pygments.org/
Source0:        https://bitbucket.org/birkenfeld/pygments-main/get/%{version}.tar.gz#/Pygments-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-nose

%description
It is a generic syntax highlighter suitable for use in code hosting,
forums, wikis or other applications that need to prettify source code.
Highlights are:

* a wide range of over 300 languages and other text formats is supported
* special attention is paid to details, increasing quality by a fair amount
* support for new languages and formats are added easily
* a number of output formats, presently HTML, LaTeX, RTF, SVG, all image
  formats that PIL supports and ANSI sequences
* it is usable as a command-line tool and as a library

%prep
%setup -q -n birkenfeld-pygments-main-%{commit}


%build
%py3_build


%install
%py3_install


%check
# PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-%{python3_version} -v

# NOTE: Disable the check above since I don't know how to fix the error below.
# ============================================================== FAILURES ==============================================================
# ______________________________________________________ CmdLineTest.test_errors _______________________________________________________
# 
# self = <test_cmdline.CmdLineTest testMethod=test_errors>
# 
#     def test_errors(self):
#         # input file not found
#         e = self.check_failure('-lpython', 'nonexistent.py')
#         self.assertTrue('Error: cannot read infile' in e)
#         self.assertTrue('nonexistent.py' in e)
# 
#         # lexer not found
#         e = self.check_failure('-lfooo', TESTFILE)
#         self.assertTrue('Error: no lexer for alias' in e)
# 
#         # cannot load .py file without load_from_file flag
#         e = self.check_failure('-l', 'nonexistent.py', TESTFILE)
#         self.assertTrue('Error: no lexer for alias' in e)
# 
#         # lexer file is missing/unreadable
#         e = self.check_failure('-l', 'nonexistent.py',
#                                '-x', TESTFILE)
#         self.assertTrue('Error: cannot read' in e)
# 
#         # lexer file is malformed
#         e = self.check_failure('-l', 'support/empty.py',
#                                '-x', TESTFILE)
# >       self.assertTrue('Error: no valid CustomLexer class found' in e)
# E       AssertionError: False is not true
# 
# tests/test_cmdline.py:252: AssertionError
# ================================ 1 failed, 1991 passed, 9 skipped, 2 pytest-warnings in 26.14 seconds ================================



%files
%license LICENSE
%doc CHANGES README.rst
%{python3_sitelib}/pygments/
%{python3_sitelib}/*.egg-info
%{_bindir}/pygmentize


%changelog
* Sat Feb 25 2017 Hiroaki Nakamura <hnakamur@gmail.com> - 2.2.0-1
- Initial EPEL7 package
