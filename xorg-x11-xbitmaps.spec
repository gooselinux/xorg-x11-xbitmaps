%define pkgname xbitmaps

%define debug_package %{nil}

Summary: X.Org X11 application bitmaps
Name: xorg-x11-%{pkgname}
Version: 1.0.1
Release: 9.1%{?dist}
License: MIT
Group: User Interface/X
URL: http://www.x.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0: ftp://ftp.x.org/pub/individual/data/xbitmaps-%{version}.tar.bz2

Provides: xbitmaps
Provides: xbitmaps-devel

%description
X.Org X11 application bitmaps

%prep
%setup -q -n xbitmaps-%{version}

%build
# Build xbitmaps
%configure
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
#%doc
%dir %{_includedir}/X11/bitmaps
%{_includedir}/X11/bitmaps/*
# Symlink for devel linking
%{_includedir}/X11/bitmaps
%{_libdir}/pkgconfig/xbitmaps.pc

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.0.1-9.1
- Rebuilt for RHEL 6

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 23 2009 Adam Jackson <ajax@redhat.com> 1.0.1-8
- Un-require xorg-x11-filesystem

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jul 15 2008 Adam Jackson <ajax@redhat.com> 1.0.1-6
- Fix license tag.

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.1-5.1
- Autorebuild for GCC 4.3

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - sh: line 0: fg: no job control
- rebuild

* Wed Jun 21 2006 Mike A. Harris <mharris@redhat.com> 1.0.1-4
- Bump release and rebuild for FC6.

* Thu Mar 02 2006 Mike A. Harris <mharris@redhat.com> 1.0.1-3
- Made package arch specific due to pkgconfig files being placed in lib64
  if the noarch packages manage to get built on x86_64/ppc64/s390x.

* Wed Mar 01 2006 Mike A. Harris <mharris@redhat.com> 1.0.1-2
- Cleaned up file manifest.
- Made package noarch, as it is just header files.
- Disable debuginfo processing, as there are no ELF objects in package.

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> 1.0.1-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> 1.0.1-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Wed Jan 18 2006 Mike A. Harris <mharris@redhat.com> 1.0.1-1
- Updated to xbitmaps 1.0.1 from X11R7.0

* Sat Dec 17 2005 Mike A. Harris <mharris@redhat.com> 1.0.0-1
- Updated to xbitmaps 1.0.0 from X11R7 RC4.

* Wed Nov 23 2005 Mike A. Harris <mharris@redhat.com> 0.99.1-4
- Updated dep to "Requires(pre): xorg-x11-filesystem >= 0.99.2-3" for new fix.
- Moved bitmap files back into the upstream default of _includedir (#173665).

* Mon Nov 21 2005 Mike A. Harris <mharris@redhat.com> 0.99.1-3
- Added "Requires(pre): xorg-x11-filesystem >= 0.99.2-1" to attempt to
  workaround bug( #173384).

* Fri Nov 11 2005 Mike A. Harris <mharris@redhat.com> 0.99.1-2
- Clean up specfile.

* Fri Nov 11 2005 Mike A. Harris <mharris@redhat.com> 0.99.1-1
- Updated to xbitmaps 0.99.1 from X11R7 RC2

* Fri Aug 26 2005 Mike A. Harris <mharris@redhat.com> 0.99.0-1
- Initial build.
