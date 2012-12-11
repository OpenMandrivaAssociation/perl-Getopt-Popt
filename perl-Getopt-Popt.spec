%define	upstream_name    Getopt-Popt
%define	upstream_version 0.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	3

Summary:	Perl interface to the popt(3)library
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{dir_name}/
Source0:    http://cpan.uwinnipeg.ca/cpan/authors/id/J/JA/JAMESB/%{upstream_name}-%{upstream_version}.tar.bz2
Patch0:		Getopt-Popt-0.02-x86_64-build.patch
Patch1:		Getopt-Popt-0.02-fix-testsuite.diff

BuildRequires:	perl-devel
BuildRequires:  popt-devel

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
The Getopt::Popt module provides a Perl OO interface to the popt(3) library,
a library to parse command-line arguments. Popt is similar to getopt, but with
many new features.
This module provides a method for almost all of the popt library functions,
the rest are on the TODO list.
This release should be considered a beta and may have a bug or two.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p0
%patch1 -p0

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="$RPM_OPT_FLAGS"

%check
LC_ALL=C %make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README Changes example.pl
%{_mandir}/*/*
%{perl_vendorarch}/*


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.20.0-3
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.20.0-2mdv2011.0
+ Revision: 555873
- rebuild for perl 5.12

* Fri Feb 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.20.0-1mdv2010.1
+ Revision: 504806
- rebuild using %%perl_convert_version

  + Thierry Vignaud <tv@mandriva.org>
    - patch 1: workaround testsuite testing stupid constants
    - rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.02-7mdv2009.0
+ Revision: 257103
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.02-5mdv2008.1
+ Revision: 152087
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.02-4mdv2008.0
+ Revision: 86464
- rebuild


* Wed Jul 26 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 07/26/06 20:05:14 (42235)
- push test into check section

* Wed Jul 26 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 07/26/06 20:02:36 (42234)
- rebuild

* Wed Jul 26 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 07/26/06 19:59:27 (42229)
Import perl-Getopt-Popt

* Fri Jul 08 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.02-2mdk
- patch 0: fix testsuite on 64bit platforms

* Sun Jan 23 2005 Sylvie Terjan <erinmargault@zarb.org> 0.02-1mdk
-initial specfile

