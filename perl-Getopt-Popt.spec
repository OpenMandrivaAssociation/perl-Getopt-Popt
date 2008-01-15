%define	real_name Getopt::Popt
%define dir_name Getopt-Popt
%define	name	perl-%{dir_name}
%define	version	0.02
%define	release	%mkrel 5

Summary:	Perl interface to the popt(3)library
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Perl
Source:		http://cpan.uwinnipeg.ca/cpan/authors/id/J/JA/JAMESB/%{dir_name}-%{version}.tar.bz2
Patch0:		Getopt-Popt-0.02-x86_64-build.patch
URL:		http://search.cpan.org/dist/%{dir_name}/
BuildRequires:	perl-devel
BuildRequires:  popt-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot
Requires:	perl

%description
The Getopt::Popt module provides a Perl OO interface to the popt(3) library,
a library to parse command-line arguments. Popt is similar to getopt, but with
many new features.
This module provides a method for almost all of the popt library functions,
the rest are on the TODO list.
This release should be considered a beta and may have a bug or two.

%prep
%setup -q -n %{dir_name}-%{version}
%patch0 -p0

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="$RPM_OPT_FLAGS"

%check
LC_ALL=C make test

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


