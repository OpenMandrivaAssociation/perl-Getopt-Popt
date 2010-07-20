%define	upstream_name    Getopt-Popt
%define	upstream_version 0.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

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
